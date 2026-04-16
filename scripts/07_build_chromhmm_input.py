import pandas as pd
from pathlib import Path

samples = pd.read_csv("data/processed/samples.csv")
out = Path("data/processed/chromhmm")
out.mkdir(parents=True, exist_ok=True)

rows = []
for _, r in samples.iterrows():
    rows.append({"sample_id": r["sample_id"], "bam": f"data/raw/{r['sample_id']}", "sex": r["sex"], "perturbation": r["perturbation"]})

pd.DataFrame(rows).to_csv(out / "sample_manifest.csv", index=False)