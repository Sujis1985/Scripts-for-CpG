import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt

files = glob.glob("results/*CpGOE.csv")

data = []

for f in files:
    species = f.split("/")[-1].replace("_CpGOE.csv","")
    df = pd.read_csv(f)
    df["Species"] = species
    data.append(df)

df = pd.concat(data)

plt.figure(figsize=(10,6))

sns.violinplot(
    x="Species",
    y="CpG_OE",
    data=df,
    inner="box"
)

plt.xticks(rotation=45)
plt.ylabel("CpG Observed / Expected")
plt.title("Distribution of CpG observed/expected ratios across millet coding sequences")

plt.tight_layout()
plt.savefig("figures/Figure4_CpGOE_distribution.png", dpi=600)
plt.close()
