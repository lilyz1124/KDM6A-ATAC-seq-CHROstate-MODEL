import pandas as pd
from pathlib import Path
import subprocess

samples = pd.read_csv("data/processed/samples_checked.csv")
peak_dir = Path("data/processed/peaks")
peak_dir.mkdir(parents=True, exist_ok=True)

for _, r in samples.iterrows():
    frag = Path(r["fragments_path"])
    if not frag.exists():
        continue
    out_prefix = peak_dir / r["sample_id"]
    cmd = [
        "macs2", "callpeak",
        "-t", str(frag),
        "-f", "BEDPE",
        "-g", "mm",
        "--nomodel",
        "--shift", "-100",
        "--extsize", "200",
        "-n", r["sample_id"],
        "--outdir", str(peak_dir)
    ]
    subprocess.run(cmd, check=False)