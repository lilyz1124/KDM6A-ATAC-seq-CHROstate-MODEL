import pandas as pd, numpy as np, torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import yaml, joblib

cfg = yaml.safe_load(open("config.yaml"))
X = pd.read_csv("data/processed/feature_matrix.csv").fillna(0)
y = pd.read_csv("data/processed/labels.csv")["label"].values

class DS(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X.values, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
    def __len__(self): return len(self.y)
    def __getitem__(self, i): return self.X[i], self.y[i]

trX, vaX, try_, vay = train_test_split(X, y, test_size=0.2, random_state=cfg["model"]["seed"], stratify=y)
train = DataLoader(DS(trX, try_), batch_size=cfg["model"]["batch_size"], shuffle=True)
val = DataLoader(DS(vaX, vay), batch_size=cfg["model"]["batch_size"])

class Net(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d, 128), nn.ReLU(), nn.Dropout(cfg["model"]["dropout"]),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, 1)
        )
    def forward(self, x): return self.net(x).squeeze(-1)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = Net(X.shape[1]).to(device)
opt = torch.optim.Adam(model.parameters(), lr=cfg["model"]["lr"])
loss_fn = nn.BCEWithLogitsLoss()

for epoch in range(cfg["model"]["epochs"]):
    model.train()
    for xb, yb in train:
        xb, yb = xb.to(device), yb.to(device)
        logits = model(xb)
        loss = loss_fn(logits, yb)
        opt.zero_grad()
        loss.backward()
        opt.step()

model.eval()
preds, truth = [], []
with torch.no_grad():
    for xb, yb in val:
        xb = xb.to(device)
        logits = model(xb).cpu().numpy()
        preds.extend(logits.tolist())
        truth.extend(yb.numpy().tolist())

auc = roc_auc_score(truth, preds) if len(set(truth)) > 1 else np.nan
torch.save(model.state_dict(), "models/multimodal.pt")
joblib.dump({"auc": auc, "columns": X.columns.tolist()}, "models/multimodal_meta.pkl")