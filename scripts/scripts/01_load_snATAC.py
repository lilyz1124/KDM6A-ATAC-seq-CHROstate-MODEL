import pandas as pd

samples = pd.read_csv("data/metadata/samples.csv")
samples["fragments_path"] = samples["fragments_path"].astype(str)
samples.to_csv("data/processed/samples_checked.csv", index=False)