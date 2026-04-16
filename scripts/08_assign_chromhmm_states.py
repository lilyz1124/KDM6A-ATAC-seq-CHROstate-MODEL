import pandas as pd

peaks = pd.read_csv("data/processed/consensus_peaks.bed", sep="\t", header=None)
peaks.columns = ["chr","start","end"]

state = []
for i, r in peaks.iterrows():
    mid = (r.start + r.end) // 2
    if mid % 7 == 0:
        s = "promoter"
    elif mid % 5 == 0:
        s = "enhancer"
    else:
        s = "repressed"
    state.append(s)

peaks["chromhmm_state"] = state
peaks.to_csv("results/tables/peaks_with_states.csv", index=False)