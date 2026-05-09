from Bio import SeqIO
import pandas as pd
import sys

fasta = sys.argv[1]
out = sys.argv[2]

rows = []

for rec in SeqIO.parse(fasta, "fasta"):
    seq = str(rec.seq).upper()
    L = len(seq)

    c = seq.count("C")
    g = seq.count("G")
    cpg = seq.count("CG")

    if c > 0 and g > 0:
        cpg_oe = (cpg * L) / (c * g)
    else:
        cpg_oe = None

    rows.append([rec.id, cpg, cpg_oe])

df = pd.DataFrame(rows, columns=["Gene","CpG_count","CpG_OE"])
df.to_csv(out, index=False)

print("✅ CpG O/E calculated")
