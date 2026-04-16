import pandas as pd
import pyranges as pr
from pathlib import Path

peak_dir = Path("data/processed/peaks")
beds = list(peak_dir.glob("*.narrowPeak"))

grs = []
for b in beds:
    try:
        df = pd.read_csv(b, sep="\t", header=None, usecols=[0,1,2])
        df.columns = ["Chromosome","Start","End"]
        grs.append(pr.PyRanges(df))
    except Exception:
        pass

if not grs:
    raise SystemExit("No peak files found.")

merged = grs[0]
for g in grs[1:]:
    merged = merged.concatenate(g)
merged = merged.merge()

merged.df.to_csv("data/processed/consensus_peaks.bed", sep="\t", header=False, index=False)