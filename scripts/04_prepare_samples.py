import pandas as pd
from pathlib import Path

meta = pd.read_csv("data/metadata/encode_metadata.csv")
meta["sample_id"] = meta["accession"]
meta["sex"] = meta["description"].str.contains("female", case=False, na=False).map({True:"female", False:"unknown"})
meta["perturbation"] = meta["description"].str.contains("kdm6a|kdm6a", case=False, na=False).map({True:"kdm6a_related", False:"control"})
meta.to_csv("data/processed/samples.csv", index=False)
