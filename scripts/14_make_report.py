import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results/tables/kdm6a_heart_target_report.csv")
top = df["direction"].value_counts()

plt.figure(figsize=(5,4))
sns.barplot(x=top.index, y=top.values)
plt.ylabel("count")
plt.title("Kdm6a-linked target directions")
plt.tight_layout()
plt.savefig("results/figures/target_directions.png", dpi=200)