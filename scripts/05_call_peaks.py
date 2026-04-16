from pathlib import Path
import subprocess, pandas as pd

samples = pd.read_csv("data/processed/samples.csv")
outdir = Path("data/processed/peaks")
outdir.mkdir(parents=True, exist_ok=True)

for _, r in samples.iterrows():
    bam = Path("data/raw") / str(r["sample_id"])
    if bam.exists():
        bed = outdir / f"{r['sample_id']}.narrowPeak"
        cmd = f"macs2 callpeak -t {bam} -f BAM -g mm --nomodel --shift -100 --extsize 200 -n {r['sample_id']} --outdir {outdir}"
        subprocess.run(cmd, shell=True, check=False)