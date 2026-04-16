import pandas as pd

peaks = pd.read_csv("data/processed/consensus_peaks.bed", sep="\t", header=None)
peaks.columns = ["chrom","start","end"]
peaks.to_csv("data/processed/bpnet_peaks.bed", sep="\t", header=False, index=False)