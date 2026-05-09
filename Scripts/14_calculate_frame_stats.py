import pandas as pd

df = pd.read_csv("results/CpG_frame_origin_summary.csv")

df["Total"] = df["CpG_frame1_2"] + df["CpG_frame2_3"] + df["CpG_inter_codon"]

df["Frame1_2_pct"] = df["CpG_frame1_2"] / df["Total"] * 100
df["Frame2_3_pct"] = df["CpG_frame2_3"] / df["Total"] * 100
df["Inter_pct"] = df["CpG_inter_codon"] / df["Total"] * 100

df.to_csv("results/CpG_frame_origin_percentages.csv", index=False)

print("✅ Frame percentage table created")
