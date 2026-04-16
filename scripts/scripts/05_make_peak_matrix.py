import pandas as pd
from pathlib import Path

peaks = pd.read_csv("data/processed/consensus_peaks.bed", sep="\t", header=None)
peaks.columns = ["chr", "start", "end"]

samples = pd.read_csv("data/processed/samples_checked.csv")
rows = []

for _, s in samples.iterrows():
    rows.append({
        "sample_id": s["sample_id"],
        "sex": s["sex"],
        "perturbation": s["perturbation"],
        "n_peaks": len(peaks)
    })

pd.DataFrame(rows).to_csv("data/processed/peak_matrix_summary.csv", index=False)