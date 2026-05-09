import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

dfs = []

for f in glob.glob("results/*_RSCU_comparison.csv"):
    df = pd.read_csv(f)

    rich_col = [c for c in df.columns if "rich" in c.lower()][0]
    poor_col = [c for c in df.columns if "poor" in c.lower()][0]

    df["Delta_RSCU"] = df[rich_col] - df[poor_col]
    dfs.append(df[["Codon", "Delta_RSCU"]])

# Mean ΔRSCU across species
delta_df = pd.concat(dfs).groupby("Codon").mean()
delta_df = delta_df.sort_values("Delta_RSCU", ascending=False)

# Identify CpG-forming codons
is_cpg = delta_df.index.str.contains("CG")

# Prepare y-axis labels
y_labels = [
    f"{codon} ●" if flag else codon
    for codon, flag in zip(delta_df.index, is_cpg)
]

# Plot
plt.figure(figsize=(6, 10))
ax = sns.heatmap(
    delta_df[["Delta_RSCU"]],
    cmap="RdBu_r",
    center=0,
    linewidths=0.4,
    yticklabels=True,
    cbar_kws={"label": "ΔRSCU (CpG-rich − CpG-poor)"}
)

# Force all tick labels to show
ax.set_yticks(range(len(y_labels)))
ax.set_yticklabels(y_labels, rotation=0)

plt.title("Codon-level CpG-dependent usage shifts\n(● = CpG-forming codons)")
plt.xlabel("")
plt.ylabel("Codon")

plt.tight_layout()
plt.savefig("figures/Figure8A_DeltaRSCU_heatmap.png", dpi=300)
plt.close()
