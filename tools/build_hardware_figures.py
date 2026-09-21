#!/usr/bin/env python3
"""Build editable SVG figures from unchanged photos and reviewed callout layouts.

The layouts record normalized image regions and feature positions recovered
from the author's slides. Captions and instructions remain in Markdown.
No PowerPoint renderer, image editor or robot dependencies are required.
"""
import argparse
import base64
import hashlib
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCENT = '#bc420f'


def render(layout):
    width, height = layout['canvas']
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
             f'<title id="title">{escape(layout["title"])}</title>',
             f'<desc id="description">{escape(layout["description"])}</desc>',
             '<rect width="100%" height="100%" fill="white"/>',
             '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="'+ACCENT+'"/></marker></defs>']
    panels = {}
    for key, source in layout['sources'].items():
        data = (ROOT/'docs'/source['path']).read_bytes()
        if hashlib.sha256(data).hexdigest() != source['sha256']:
            raise ValueError('Source image changed: '+source['path'])
        iw, ih = source['pixels']
        uri = 'data:'+source['mime']+';base64,'+base64.b64encode(data).decode()
        parts.append(f'<defs><image id="photo-{escape(key)}" width="{iw}" height="{ih}" href="{uri}"/></defs>')
    for panel in layout['panels']:
        source = layout['sources'][panel['source']]
        iw, ih = source['pixels']
        rx, ry, rw, rh = panel.get('region', [0, 0, 1, 1])
        x, y, w = panel['position']
        h = w * rh * ih / (rw * iw)
        panels[panel['id']] = (x, y, w, h, rx, ry, rw, rh)
        parts.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h:.4f}" viewBox="{rx*iw} {ry*ih} {rw*iw} {rh*ih}" overflow="hidden"><use href="#photo-{escape(panel["source"])}"/></svg>')
        border = ACCENT if panel.get('badge') else '#c6c6c6'
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h:.4f}" fill="none" stroke="{border}" stroke-width="2"/>')
        if panel.get('badge'):
            parts.append(f'<circle cx="{x+24}" cy="{y+24}" r="19" fill="{ACCENT}" stroke="white" stroke-width="3"/><text x="{x+24}" y="{y+32}" text-anchor="middle" font-family="sans-serif" font-size="23" font-weight="bold" fill="white">{escape(panel["badge"])}</text>')
    for callout in layout['callouts']:
        x,y,w,h,rx,ry,rw,rh = panels[callout['panel']]
        px,py = callout['feature']
        cx,cy = x+(px-rx)*w/rw, y+(py-ry)*h/rh
        radius = callout.get('radius',18)
        # White halo keeps the mark readable over both dark and pale hardware.
        parts.append(f'<circle cx="{cx:.4f}" cy="{cy:.4f}" r="{radius}" fill="none" stroke="white" stroke-width="7"/><circle cx="{cx:.4f}" cy="{cy:.4f}" r="{radius}" fill="none" stroke="{ACCENT}" stroke-width="3"/>')
        if 'detail' in callout:
            dx,dy,dw,dh,*_ = panels[callout['detail']]
            startx,starty,endx,endy = cx+radius,cy,dx-7,dy+dh/2
            path = f'M {startx:.4f},{starty:.4f} C {startx+80:.4f},{starty-30:.4f} {endx-70:.4f},{endy-25:.4f} {endx:.4f},{endy:.4f}'
            parts.append(f'<path d="{path}" fill="none" stroke="white" stroke-width="7"/><path d="{path}" fill="none" stroke="{ACCENT}" stroke-width="3" marker-end="url(#arrow)"/>')
    parts.append('</svg>\n')
    return '\n'.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    layouts = json.loads((ROOT/'docs/assets/hardware-figures.json').read_text())['figures']
    catalog_path = ROOT/'docs/assets/media.json'
    catalog = json.loads(catalog_path.read_text())
    assets = {asset['id']: asset for asset in catalog['assets']}
    for layout in layouts:
        path = ROOT/'docs'/layout['output']
        rendered = render(layout)
        data = rendered.encode()
        checksum = hashlib.sha256(data).hexdigest()
        if args.check:
            if not path.exists() or path.read_text()!=rendered:
                parser.error('Figure is stale: '+layout['output'])
            if layout['id'] not in assets or assets[layout['id']]['sha256'] != checksum:
                parser.error('Figure catalog is stale: '+layout['id'])
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered)
            if layout['id'] in assets:
                assets[layout['id']].update(sha256=checksum, bytes=len(data))
    if not args.check:
        catalog_path.write_text(json.dumps(catalog, indent=2)+'\n')
    print(f'{len(layouts)} annotated hardware figures match their sources and layouts.')


if __name__ == '__main__':
    main()
