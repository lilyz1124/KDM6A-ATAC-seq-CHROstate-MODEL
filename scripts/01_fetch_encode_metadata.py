import requests, yaml, pandas as pd
from pathlib import Path

cfg = yaml.safe_load(open("config.yaml"))
rows = []

for q in cfg["encode_queries"]:
    url = "https://www.encodeproject.org/search/?type=Experiment&format=json&limit=50&searchTerm=" + requests.utils.quote(q)
    r = requests.get(url, headers={"Accept": "application/json"})
    if r.ok:
        j = r.json()
        for item in j.get("@graph", []):
            rows.append({
                "source": "ENCODE",
                "query": q,
                "accession": item.get("accession"),
                "assay": item.get("assay_title"),
                "biosample": item.get("biosample_ontology", {}).get("term_name"),
                "organism": item.get("organism", {}).get("scientific_name"),
                "description": item.get("description", "")
            })

df = pd.DataFrame(rows).drop_duplicates()
df.to_csv("data/metadata/encode_metadata.csv", index=False)