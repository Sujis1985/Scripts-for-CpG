# Scripts-for-CpG
Pipeline Overview: Genome-Wide CpG Architecture & Codon Bias
This repository contains the custom Python and Bash scripts used to investigate the relationship between synonymous codon usage bias and CpG dinucleotide architecture across six climate-resilient millet genomes. The pipeline is fully modular and maps directly to the methodology and figures presented in the manuscript.

Phase 1: Genome-wide CpG Density & Classification (Figure 1)
Calculates raw CpG density and stratifies coding sequences into functionally distinct classes.

01_calculate_density.py: Scans genome-wide coding sequences (CDS) to calculate the absolute CpG dinucleotide density per kilobase for each gene.

02_classify_genes.py: Applies species-specific quartile thresholds to classify genes into CpG-rich (≥ Q3), CpG-moderate (Q1–Q3), and CpG-poor (≤ Q1) categories.

03_plot_density.py: Generates smoothed kernel density (KDE) ridgeline plots to visualize the non-random CpG density landscapes across the genomes (Figure 1).

Phase 2: Positional CpG Distribution / Metagene Analysis (Figure 2)
Assesses the spatial distribution of CpG motifs to test for gene body–centric enrichment.

04_scan_gene_regions.py: Partitions each CDS into three equal-length relative segments (5′ region, central gene body, and 3′ region) and quantifies CpG occurrences within each bin.

05_plot_gene_regions.py: Generates metagene line profiles demonstrating the conserved enrichment of CpG motifs within internal gene body regions (Figure 2).

Phase 3: Codon Bias Across CpG Gene Classes (Figure 3)
Evaluates differences in translational optimization and codon bias metrics among the CpG architectures.

06_format_codon_data.py: Standardizes the formatting of pre-calculated Effective Number of Codons (ENC) and Codon Adaptation Index (CAI) datasets.

07_merge_codon_data.py: Integrates the codon bias metrics (ENC, CAI, GC3s) with the respective CpG gene classifications.

08_plot_codon_differences.py: Generates boxplots with raw-data strip overlays to statistically compare ENC, CAI, and GC3s across the three CpG classes (Figure 3).

Phase 4: CpG Observed/Expected (O/E) Ratios (Figure 4)
Determines whether CpG variation is driven by active enrichment/depletion or background nucleotide composition.

09_calculate_expected_cpg.py: Computes the sequence-length normalized CpG O/E ratio for each gene based on local Cytosine and Guanine frequencies.

10_plot_expected_cpg.py: Generates violin plots illustrating the broad distribution of CpG-enriched versus CpG-depleted coding sequences (Figure 4).

Phase 5: Codon-CpG Correlation & GC3 Controls (Figures 5 & 6)
Disentangles the influence of GC-content at the 3rd synonymous position (GC3s) from structural CpG architecture.

11_plot_correlations.py: Computes Spearman rank correlations between CpG density, GC3s, ENC, and CAI, visualizing the structural coupling via a heatmap (Figure 5).

12_plot_gc3_effects.py: Bins genes strictly by GC3s content (<40%, 40-60%, >60%) and generates boxplots to demonstrate that CpG variation persists independently of GC3 constraints (Figure 6).

Phase 6: Codon-Frame Origin of CpG Motifs (Figure 7)
Investigates the structural origin of CpG motifs relative to codon boundaries to determine the role of codon adjacency.

13_scan_reading_frames.py: Scans translating reading frames to classify each CpG motif as originating from positions 1-2, positions 2-3, or across inter-codon boundaries.

14_calculate_frame_stats.py: Converts raw positional occurrences into relative genome-wide percentages.

15_plot_reading_frames.py: Generates stacked bar charts highlighting the dominance of inter-codon CpG motif formation (Figure 7).

Phase 7: Relative Synonymous Codon Usage (ΔRSCU) Shifts (Figure 8)
Quantifies how synonymous codon preferences shift to accommodate or avoid CpG motifs in different gene classes.

16_extract_sequences.py & 17_run_extraction_all.sh: Python engine and Bash wrapper to dynamically extract physical FASTA sequences for the specific CpG-rich and CpG-poor gene cohorts across all species.

18_calculate_rscu.py & 19_run_rscu_all.sh: Computes standard RSCU values for the extracted cohorts.

20_compare_rscu.py: Computes the mathematical difference (ΔRSCU) between CpG-rich and CpG-poor usage preferences.

21_plot_rscu_heatmap.py: Generates a log₂-transformed ΔRSCU heatmap, specifically flagging CpG-forming codons to reveal systemic usage shifts (Figure 8A).

22_plot_rscu_bars.py: Generates grouped bar charts comparing the log₂ fold-change of CpG-forming codons versus non-CpG synonymous equivalents, grouped by amino acid (Figure 8B).
