#!/usr/bin/env python3
"""Recreate selected media from the originals without changing those originals.

Requires ffmpeg and ffprobe for videos. The ordinary documentation build does
not run this tool or require access to the source collection. Recipes and source
hashes live alongside captions in docs/assets/media.json.
"""

import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def remove_image_metadata(data):
    """Remove EXIF/text metadata while preserving encoded image samples.

    Selected sources have upright pixels. This intentionally does not resize,
    crop, rotate or recompress the photographs, or recreate slide annotations.
    """
    if data.startswith(b"\xff\xd8"):
        output = bytearray(data[:2])
        offset = 2
        while offset < len(data):
            start = offset
            if data[offset] != 255:
                raise ValueError("Invalid JPEG marker")
            while data[offset] == 255:
                offset += 1
            marker = data[offset]
            offset += 1
            if marker in (0xDA, 0xD9):  # Copy scan data and everything after it.
                output.extend(data[start:])
                return bytes(output)
            length = int.from_bytes(data[offset:offset + 2], "big")
            if length < 2 or offset + length > len(data):
                raise ValueError("Invalid JPEG segment")
            if marker not in (0xE1, 0xED, 0xFE):  # EXIF/XMP, IPTC, comments.
                output.extend(data[start:offset + length])
            offset += length
        raise ValueError("JPEG has no scan")
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        output = bytearray(data[:8])
        offset = 8
        while offset < len(data):
            length = struct.unpack(">I", data[offset:offset + 4])[0]
            kind = data[offset + 4:offset + 8]
            end = offset + length + 12
            if end > len(data):
                raise ValueError("Invalid PNG chunk")
            if kind not in (b"eXIf", b"tEXt", b"zTXt", b"iTXt"):
                output.extend(data[offset:end])
            offset = end
            if kind == b"IEND":
                return bytes(output)
        raise ValueError("PNG has no end chunk")
    raise ValueError("Only JPEG and PNG images are supported")


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin",
                    "-y", *map(str, args)], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--video-dir", type=Path, required=True,
                        help="Ignored output directory for release assets")
    parser.add_argument("--asset", action="append", default=[],
                        help="Prepare only this stable ID; may be repeated")
    args = parser.parse_args()
    catalog_path = ROOT / "docs/assets/media.json"
    catalog = json.loads(catalog_path.read_text())
    assets = [a for a in catalog["assets"] if "preparation" in a]
    if args.asset:
        missing = set(args.asset) - {a["id"] for a in assets}
        if missing:
            parser.error("No preparation recipe for: " + ", ".join(sorted(missing)))
        assets = [a for a in assets if a["id"] in args.asset]

    # Check source identities before writing any publication copy.
    for asset in assets:
        source = args.source_dir / asset["source_file"]
        if digest(source.read_bytes()) != asset["source_sha256"]:
            raise ValueError(f"Source changed: {source.name}; review it first")
        if asset.get("source_member"):
            with zipfile.ZipFile(source) as archive:
                data = archive.read(asset["source_member"])
            if digest(data) != asset["source_member_sha256"]:
                raise ValueError(f"Embedded source changed: {asset['id']}")

    args.video_dir.mkdir(parents=True, exist_ok=True)
    for asset in assets:
        source = args.source_dir / asset["source_file"]
        recipe = asset["preparation"]
        if recipe["kind"] == "image-metadata-only":
            if asset.get("source_member"):
                with zipfile.ZipFile(source) as archive:
                    data = archive.read(asset["source_member"])
            else:
                data = source.read_bytes()
            output = ROOT / "docs" / asset["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(remove_image_metadata(data))
        else:
            output = args.video_dir / asset["filename"]
            if source.resolve() == output.resolve():
                raise ValueError("Output must not replace an original")
            ffmpeg("-i", source, "-map", "0:v:0", "-an", "-map_metadata", "-1",
                   *recipe["ffmpeg_output_args"], "-movflags", "+faststart", output)
            poster = ROOT / "docs" / asset["poster"]["path"]
            poster.parent.mkdir(parents=True, exist_ok=True)
            ffmpeg("-ss", recipe["poster_seconds"], "-i", output,
                   "-frames:v", "1", "-q:v", "2", "-map_metadata", "-1", poster)
            asset["poster"]["sha256"] = digest(poster.read_bytes())
            asset["poster"]["bytes"] = poster.stat().st_size
            probe = json.loads(subprocess.check_output([
                "ffprobe", "-v", "error", "-show_streams", "-show_format",
                "-of", "json", str(output)], text=True))
            stream = next(s for s in probe["streams"] if s["codec_type"] == "video")
            asset.update(width=stream["width"], height=stream["height"],
                         duration_seconds=float(probe["format"]["duration"]),
                         video_codec=stream["codec_name"], has_audio=False)
        asset["sha256"] = digest(output.read_bytes())
        asset["bytes"] = output.stat().st_size
        print(f"{asset['id']}: {asset['bytes']:,} bytes", flush=True)
    catalog_path.write_text(json.dumps(catalog, indent=2) + "\n")


if __name__ == "__main__":
    main()
