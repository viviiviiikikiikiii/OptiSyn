# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
Step 2 – Target–Herb Association Assessment

This module evaluates the potential therapeutic association between herbs and the target disease by integrating gene overlap analysis and network-based scoring (Hscore).

Two complementary strategies are implemented:

Gene overlap analysis
Measures the similarity between herb-associated targets and disease-related genes.

Network-based scoring (Hscore)
Evaluates the regulatory influence of herb compounds within a herb–compound–disease network using PageRank.

These analyses help identify herbs with stronger biological relevance to the disease mechanism.

Method Description

To assess whether specific herbal medicines may have therapeutic relevance to the disease, the overlap rate was calculated to measure the intersection between herb targets and disease-associated genes.

Additionally, an integrated scoring metric (Hscore) was introduced to evaluate the global regulatory potential of herbs within a biological network.

The Hscore was derived from a multi-layer herb–compound–disease network using:

PageRank algorithm

two-step random walk strategy

Herbs containing more bioactive compounds tend to regulate a broader set of disease-related targets and therefore exert stronger network-level influence.

Repository Structure
Step2_TargetHerb_Assessment
│
├── input/
│   ├── disease_targets
│   │   └── gene0.txt
│   │
│   ├── herb_targets
│   │   ├── herb1.txt
│   │   ├── herb2.txt
│   │   └── ...
│   │
│   └── network_data
│       └── PR.csv
│
├── scripts/
│   ├── Gene_overlap_counter.R
│   └── PageRank.R
│
├── results/
│   ├── common_genes_results.csv
│   └── pagerank_scores.csv
│
└── README.md
Script Descriptions
1. Gene_overlap_counter.R

Calculates the number of overlapping genes between disease-associated targets and herb targets.

Purpose

Identify herbs that share biological targets with the disease.

Input
input/disease_targets/gene0.txt

Disease-associated target genes.

input/herb_targets/*.txt

Target genes for each herb.

Output
results/common_genes_results.csv

Example output:

Herb	Overlapping genes
herb1.txt	12
herb2.txt	8
herb3.txt	15
Core Logic
target_genes <- readLines(target_file)

current_genes <- readLines(file)

common_genes <- intersect(target_genes, current_genes)

common_count <- length(common_genes)
2. PageRank.R

Computes PageRank scores for nodes in the herb–compound–disease network.

Purpose

Evaluate the global regulatory influence of herbs and compounds within the biological network.

Input
input/network_data/PR.csv

Edge list describing network relationships.

Example:

nodeA,nodeB
nodeB,nodeC
nodeC,nodeD
Workflow

Construct adjacency matrix

Convert adjacency matrix to transition probability matrix

Compute PageRank via eigenvector decomposition

Output
results/pagerank_scores.csv

Example:

Node	PageRank
node1	0.023
node2	0.017
Interpretation of Results

Two complementary indicators are generated:

1️⃣ Gene Overlap Score

Measures direct molecular similarity between herb targets and disease genes.

Higher overlap suggests stronger biological relevance.

2️⃣ Hscore (Network Influence)

Reflects the global regulatory potential of herbs in the biological network.

Herbs with:

more bioactive compounds

stronger network connectivity

tend to show higher Hscores.

Position in the Overall Pipeline

This module corresponds to Step 2 in the full computational pipeline.

Step1  Herb frequency analysis
Step2  Target–herb association assessment
Step3  Network proximity analysis
Step4  Herb co-administration analysis
Step5  Compound clustering
Step6  GCN synergy prediction
Reproducibility

To reproduce the analysis:

Step 1

Place input files into the input/ directory.

Step 2

Run the scripts:

Rscript scripts/Gene_overlap_counter.R
Rscript scripts/PageRank.R
Step 3

Results will be generated in:

results/
Notes

Herb targets were collected from TCMSP and DrugBank databases.

Target genes were standardized using UniProt.

Network influence scores contribute to the integrated Hscore calculation used in later modeling steps.
