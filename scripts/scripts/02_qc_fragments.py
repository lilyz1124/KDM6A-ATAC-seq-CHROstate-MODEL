import pandas as pd
from pathlib import Path

samples = pd.read_csv("data/processed/samples_checked.csv")
outdir = Path("data/processed/qc")
outdir.mkdir(parents=True, exist_ok=True)

qc_rows = []
for _, r in samples.iterrows():
    frag = Path(r["fragments_path"])
    if not frag.exists():
        continue
    n_lines = 0
    with open(frag, "rt") as f:
        for _ in f:
            n_lines += 1
    qc_rows.append({
        "sample_id": r["sample_id"],
        "fragments_path": str(frag),
        "n_fragment_lines": n_lines,
        "sex": r["sex"],
        "perturbation": r["perturbation"]
    })

pd.DataFrame(qc_rows).to_csv(outdir / "fragment_qc.csv", index=False)