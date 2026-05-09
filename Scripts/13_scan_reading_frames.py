from Bio import SeqIO
import pandas as pd
import glob
import os

# Assuming fasta files are in the main directory
files = glob.glob("*_valid.fasta")
rows = []

for fasta in files:
    species = os.path.basename(fasta).replace("_valid.fasta", "")
    frame12 = 0
    frame23 = 0
    inter = 0

    for rec in SeqIO.parse(fasta, "fasta"):
        seq = str(rec.seq).upper()

        # CpG at codon position 1-2
        for i in range(0, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon[0:2] == "CG":
                frame12 += 1

        # CpG at codon position 2-3
        for i in range(0, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon[1:3] == "CG":
                frame23 += 1

        # CpG across codon boundary
        for i in range(2, len(seq)-1, 3):
            if seq[i:i+2] == "CG":
                inter += 1

    rows.append([species, frame12, frame23, inter])

df = pd.DataFrame(rows, columns=[
    "Species", "CpG_frame1_2", "CpG_frame2_3", "CpG_inter_codon"
])

os.makedirs("results", exist_ok=True)
df.to_csv("results/CpG_frame_origin_summary.csv", index=False)

print("✅ CpG frame scan completed")
