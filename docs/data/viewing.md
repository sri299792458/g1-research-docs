# Inspect the shared datasets

Use this page to open the five August 25 episodes without installing robot
control or planning software. The [downloads](recording.md#dataset-downloads)
also include a separate calibration archive; it is not a LeRobot dataset.

## Extract and check the collection

Download the stacking ZIP and its checksum file from the shared Drive folder.
Compare the ZIP's `sha256sum` with the supplied checksum, then extract it.
Keep `meta/`, `data/` and `videos/` together. The archive README identifies the
source runs and explains the included checksums.

Locate the directory containing `meta/info.json`; call it
`g1_august25_stacking` below. Set `G1_DATASETS` to its **absolute parent path**, so
the layout is:

```text
/path/to/datasets/
└── g1_august25_stacking/
    ├── meta/info.json
    ├── data/
    └── videos/
```

Check that `meta/info.json` reports 5 episodes, 8,272 frames and 15 FPS.
The [episode table](recording.md#august-25-demonstration-export) maps indices 0–4
to retained run IDs. These are completed recording boundaries; inspect physical
placement separately before assigning a task-success label.

## Start a local browser viewer

This setup uses the lab's [LeRobot dataset visualizer](https://github.com/RPM-lab-UMN/lerobot-dataset-visualizer/tree/67aec1afdf7202abc509f6aeb39aef8a076af11e)
and SPARK's small HTTP dataset server. You need Python with `venv`, Node.js,
Bun, Git and `curl`. The three processes have different jobs:

| Process | Local address | Purpose |
|---|---|---|
| Dataset server | `127.0.0.1:8879` | Serves the extracted metadata, Parquet and video files |
| Video backend | `127.0.0.1:7861` | Makes the encoded depth video browser-decodable |
| Viewer | `127.0.0.1:3000` | Displays episodes, video and signal plots |

Prepare a new checkout:

```bash
git clone https://github.com/RPM-lab-UMN/lerobot-dataset-visualizer.git
cd lerobot-dataset-visualizer
git switch --detach 67aec1afdf7202abc509f6aeb39aef8a076af11e
bun install --frozen-lockfile
python3 -m venv backend/.venv
backend/.venv/bin/python -m pip install -r backend/requirements.txt
curl -fL -o local_dataset_server.py \
  https://raw.githubusercontent.com/RPM-lab-UMN/spark-data-collection/be284c2f8138f383d260526f68613c7a28d364d4/data_pipeline/local_dataset_server.py
```

**Terminal 1 — serve the dataset**, from the viewer checkout. Replace the path:

```bash
export G1_DATASETS=/absolute/path/to/datasets
python3 local_dataset_server.py --root "$G1_DATASETS" --port 8879
```

**Terminal 2 — start depth playback support**, from the same checkout:

```bash
cd backend
.venv/bin/uvicorn app:app --host 127.0.0.1 --port 7861
```

**Terminal 3 — start the viewer**, from the checkout root. Use the same dataset
parent path as Terminal 1:

```bash
export G1_DATASETS=/absolute/path/to/datasets
DATASET_URL=http://127.0.0.1:8879/datasets \
VIDEO_BACKEND_URL=http://127.0.0.1:7861 \
LOCAL_DATASET_ROOT="$G1_DATASETS" \
NEXT_PUBLIC_ANNOTATE_BACKEND_URL= \
bun run dev --hostname 127.0.0.1 --port 3000
```

Open **<http://127.0.0.1:3000/local/g1_august25_stacking/0>**. This address works
on the machine running the viewer; it is not a public dataset link. The sidebar
should show five episodes. Annotation writes are not enabled by these commands.
Stop each process with Ctrl+C when finished.

The pinned public viewer was checked against this dataset using existing local
dependencies: five episodes were listed and both video streams decoded. This is
not a clean-machine dependency installation test. The [walkthrough video](recording.md#inspecting-an-exported-dataset)
shows a different, 33-episode export with additional local viewer changes;
its exact display is not the reproduction target here.

## What to inspect first

1. Select an episode and compare RGB movement with the state and action traces.
   Measured state and commanded action can differ; that difference is not
   automatically a calibration error.
2. Seek to approach, close, lift, placement and return. Check what is actually
   visible before labeling contact or successful placement.
3. Use the named features in `meta/info.json` to interpret arrays. Pressure is
   raw counts, and command gains are not measured effort. [Recorded signals](recording.md#the-lerobot-representation)
   explains the representation and sampling limits.
4. Consult the archive's conversion records for omissions and timing bounds.
   Neither video playback nor a completed task field proves a complete raw bag
   or normal final ownership handback.

Depth is a derived, lossy training representation. The backend creates a
colored playback copy because the stored grayscale depth codec is not directly
browser-compatible. Its display colors do not replace metric depth decoding
or the original calibration images.

| Symptom | Check |
|---|---|
| Dataset not found | Open `http://127.0.0.1:8879/datasets/local/g1_august25_stacking/resolve/main/meta/info.json`; a 404 usually means the root or directory name is wrong |
| RGB plays but depth does not | Backend is running, `av` installed successfully, and `LOCAL_DATASET_ROOT` names the same absolute parent directory |
| Viewer requests Hugging Face instead of local files | Restart the frontend with `DATASET_URL` including `/datasets` |
| Layout differs from the walkthrough | Confirm the public viewer revision; the video includes local extensions |

## Inspect the calibration archive separately

Read its README and keep the two capture sessions, selected fitting inputs and
bundle together. The PNGs preserve the source pixels used for calibration;
measurement metadata supplies joint state, corner observations and grouping.
Use [calibration workflow](../calibration/workflow.md) and
[results](../calibration/results.md#the-august-12-stacking-baseline) to understand
the bundle. No calibration-to-LeRobot exporter has been produced, and the
stacking viewer instructions above do not apply to those capture folders.
