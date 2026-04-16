import pandas as pd
import numpy as np

df = pd.read_csv("results/tables/peaks_with_states.csv")
states = pd.get_dummies(df["chromhmm_state"], prefix="state")
X = pd.concat([df[["start","end"]].reset_index(drop=True), states.reset_index(drop=True)], axis=1)
X.to_csv("data/processed/feature_matrix.csv", index=False)

y = np.random.randint(0, 2, size=len(X))
pd.DataFrame({"label": y}).to_csv("data/processed/labels.csv", index=False)