import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

dfs = []
for f in glob.glob("results/*_CpG_density.csv"):
    species = f.split("/")[-1].replace("_CpG_density.csv", "").replace("_", " ")
    df = pd.read_csv(f)
    df["Species"] = species
    dfs.append(df)

df_all = pd.concat(dfs)

# Global quartiles (used for CpG classification)
q1 = df_all["CpG_density_per_kb"].quantile(0.25)
q3 = df_all["CpG_density_per_kb"].quantile(0.75)

plt.figure(figsize=(10, 8))
sns.kdeplot(
    data=df_all,
    x="CpG_density_per_kb",
    hue="Species",
    fill=True,
    alpha=0.35,          
    linewidth=1.2,
    common_norm=False
)

# Reference lines
plt.axvline(q1, color="black", linestyle="--", linewidth=1)
plt.axvline(q3, color="black", linestyle="--", linewidth=1)

# Annotation
plt.text(q3 + 5, plt.ylim()[1]*0.8, "CpG-rich genes →", fontsize=11)
plt.text(q1 - 45, plt.ylim()[1]*0.8, "← CpG-poor genes", fontsize=11)

plt.xlabel("CpG density per kb (coding sequences)")
plt.ylabel("Density")
plt.title("Non-random CpG density landscapes across millet genomes")

plt.xlim(left=0)
plt.tight_layout()
plt.savefig("figures/Figure1_CpG_density_ridgeline.png", dpi=300)
plt.close()
