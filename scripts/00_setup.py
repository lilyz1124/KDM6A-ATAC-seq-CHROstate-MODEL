from pathlib import Path

for p in [
    "data/raw","data/metadata","data/processed","data/external",
    "models","results/tables","results/figures","results/tracks","scripts/bpnet"
]:
    Path(p).mkdir(parents=True, exist_ok=True)