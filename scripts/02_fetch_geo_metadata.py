import requests, yaml, pandas as pd
from pathlib import Path

cfg = yaml.safe_load(open("config.yaml"))
rows = []

for term in cfg["geo_queries"]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=" + requests.utils.quote(term) + "&retmode=json&retmax=20"
    r = requests.get(url)
    if r.ok:
        data = r.json().get("esearchresult", {}).get("idlist", [])
        for gse_id in data:
            rows.append({"source":"GEO","query":term,"gse_id":gse_id})

pd.DataFrame(rows).to_csv("data/metadata/geo_hits.csv", index=False)