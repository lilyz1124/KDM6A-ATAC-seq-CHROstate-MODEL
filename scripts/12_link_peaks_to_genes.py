import pandas as pd

peaks = pd.read_csv("results/tables/peaks_with_states.csv")
genes = pd.read_csv("data/processed/genes_tss.bed", sep="\t", header=None, names=["chr","start","end","gene"])

rows = []
for _, p in peaks.iterrows():
    nearby = genes[(genes.chr == p.chr) & (genes.start.between(p.start - 100000, p.end + 100000))]
    for _, g in nearby.iterrows():
        rows.append({
            "chr": p.chr,
            "peak_start": p.start,
            "peak_end": p.end,
            "state": p.chromhmm_state,
            "gene": g.gene,
            "distance": abs(int((p.start + p.end)/2) - int(g.start))
        })

pd.DataFrame(rows).to_csv("results/tables/peak_gene_links.csv", index=False)