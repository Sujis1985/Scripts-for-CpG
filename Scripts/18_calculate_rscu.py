from Bio import SeqIO
from collections import defaultdict
import sys
import pandas as pd

fasta = sys.argv[1]
out_csv = sys.argv[2]

genetic_code = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G"
}

codon_count = defaultdict(int)
aa_count = defaultdict(int)

for record in SeqIO.parse(fasta, "fasta"):
    seq = str(record.seq)
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        if codon in genetic_code and genetic_code[codon] != "*":
            aa = genetic_code[codon]
            codon_count[codon] += 1
            aa_count[aa] += 1

rscu = {}
for codon, count in codon_count.items():
    aa = genetic_code[codon]
    synonymous = [c for c in genetic_code if genetic_code[c] == aa]
    expected = aa_count[aa] / len(synonymous)
    rscu[codon] = round(count / expected, 4) if expected > 0 else 0

df = pd.DataFrame(list(rscu.items()), columns=["Codon","RSCU"])
df.to_csv(out_csv, index=False)

print(f"✅ RSCU calculated for {fasta}")
