import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import os

files = glob.glob("results/*_CpG_density.csv")
all_data = []

for f in files:
    species = os.path.basename(f).replace("_CpG_density.csv", "")
    
    density = pd.read_csv(f)
    codon = pd.read_csv(f"results/{species}_Objective2_codonbias_clean.csv")

    merged = pd.merge(density, codon, on="GeneID")
    merged["Species"] = species
    all_data.append(merged)

df = pd.concat(all_data)

corr = df[["CpG_density_per_kb","GC3s","ENC","CAI"]].corr(method="spearman")

plt.figure(figsize=(6,5))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    center=0
)

plt.title("Correlation between CpG density and codon usage metrics")
plt.tight_layout()

# Ensure figures directory exists
os.makedirs("figures", exist_ok=True)
plt.savefig("figures/Figure5_CpG_codon_correlation_heatmap.png", dpi=300)

print("✅ Correlation analysis completed")
