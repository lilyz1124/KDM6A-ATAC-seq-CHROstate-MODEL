import joblib, pandas as pd
meta = joblib.load("models/multimodal_meta.pkl")
pd.DataFrame([meta]).to_csv("results/tables/model_metrics.csv", index=False)