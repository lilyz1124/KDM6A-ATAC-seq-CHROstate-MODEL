import pandas as pd

links = pd.read_csv("results/tables/peak_gene_links.csv")
expr = pd.read_csv("data/processed/differential_expression.csv")

m = links.merge(expr, on="gene", how="left")
m["direction"] = m["log2FC"].apply(lambda x: "up" if x > 0 else "down" if x < 0 else "ns")
m.to_csv("results/tables/kdm6a_heart_target_report.csv", index=False)