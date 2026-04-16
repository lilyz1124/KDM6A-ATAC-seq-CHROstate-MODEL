import pandas as pd, requests, os
from pathlib import Path
from tqdm import tqdm

enc = pd.read_csv("data/metadata/encode_metadata.csv")
raw = Path("data/raw")
raw.mkdir(parents=True, exist_ok=True)

def download(url, out):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(out, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

for acc in tqdm(enc["accession"].dropna().unique()):
    api = f"https://www.encodeproject.org/experiments/{acc}/?format=json"
    r = requests.get(api, headers={"Accept": "application/json"})
    if not r.ok:
        continue
    exp = r.json()
    for f in exp.get("files", []):
        fmt = f.get("file_format")
        if fmt in {"bam","bigWig","bed","fastq"}:
            href = f.get("href")
            if href:
                url = "https://www.encodeproject.org" + href
                out = raw / f.get("accession", href.split("/")[-1])
                if not out.exists():
                    try:
                        download(url, out)
                    except Exception:
                        pass