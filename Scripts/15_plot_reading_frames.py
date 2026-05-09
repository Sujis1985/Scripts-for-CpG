import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/CpG_frame_origin_percentages.csv")
df.set_index("Species", inplace=True)

df[["Frame1_2_pct","Frame2_3_pct","Inter_pct"]].plot(
    kind="bar",
    stacked=True,
    figsize=(10,6),
    colormap="viridis"
)

plt.ylabel("Percentage of CpG motifs")
plt.title("Relative contributions of codon frames to CpG motif formation")
plt.legend(["Codon positions 1–2", "Codon positions 2–3", "Inter-codon CpG"], loc="upper right")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("figures/Figure7_CpG_frame_origin.png", dpi=600)

print("✅ Figure 7 created")
