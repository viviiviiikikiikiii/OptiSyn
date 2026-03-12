# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
Network Proximity Analysis for Herb–Disease Target Association

This repository contains the Python implementation used to evaluate the network proximity between herbal targets and disease-associated genes within a protein–protein interaction (PPI) network.

The method quantifies the functional relationship between herbal remedies and disease mechanisms based on the mean shortest distance (SAB) and its degree-preserving randomization Z-score, following the network pharmacology framework described in previous studies.

Method Overview

Genes associated with herbal compounds tend to form coherent modules within the protein–protein interaction (PPI) network. The network proximity between herb targets and disease-associated genes can therefore indicate the functional similarity between herbal mechanisms and disease pathways.

This repository implements the following core metrics:

1. Mean Shortest Distance (SAB)

The network distance between two target sets is defined as the average shortest path length between nodes from the two sets.

Saa: average distance within herb target set A

Sbb: average distance within herb target set B

Sab: average distance between target sets A and B

The normalized proximity score is calculated as:

SAB = dAB − (dAA + dBB) / 2

Where:

dAB = mean shortest distance between herb A and herb B targets

dAA, dBB = internal shortest distances within each target set

Lower SAB values indicate closer functional proximity within the PPI network.

2. Z-score for Network Proximity

To assess statistical significance, a degree-preserving randomization strategy is used.

For each herb–disease pair:

Random target sets are generated while preserving node degree distribution.

Random SAB values are computed (50 iterations).

A Z-score is calculated:

Z = (dAB − mean_random) / var_random

A negative Z-score indicates that herb targets are significantly closer to disease genes than expected by chance.

3. Key Node Identification

Two additional analyses are performed to identify important mediating genes:

Shortest Distance Ranking

All nodes in the PPI network are ranked based on their total shortest distance to herb and disease target sets.

This helps identify potential intermediate genes connecting herb targets and disease modules.

Flow Centrality (FC)

For each pair of targets:

All shortest paths between herb targets and disease genes are enumerated.

Intermediate nodes are counted.

Nodes appearing frequently in shortest paths receive higher FC scores.

These nodes may represent key regulators or bridging genes in herb–disease interactions.

Repository Structure
.
├── PPI_symbol_noego.txt        # PPI network edge list
├── gene/                       # Herb target gene lists
├── tar/                        # Disease target gene lists
├── sab11.csv                   # SAB results
├── zab5.csv                    # Z-score results
├── *_shortest.csv              # Node shortest-distance ranking
├── *_fc.csv                    # Flow centrality results
└── sab_analysis.py             # Main analysis script
Input Data
PPI Network
PPI_symbol_noego.txt

Format:

ProteinA,ProteinB
ProteinC,ProteinD
...
Herb Target Genes

Located in:

gene/

Format:

gene
AKT1
MAPK1
STAT3
...
Disease Target Genes

Located in:

tar/

Format:

targets
IL6
TNF
VEGFA
...
Requirements

Python packages:

networkx
numpy
pandas

Install via:

pip install networkx numpy pandas
Running the Analysis

Update the working directory in the script:

os.chdir("D:/R/sab/")

Then run:

python sab_analysis.py

The script will compute:

SAB values

Z-score proximity

Shortest path node ranking

Flow centrality nodes

Results will be exported as CSV files.

Outputs
File	Description
sab11.csv	Herb–herb network proximity score
zab5.csv	Herb–disease proximity Z-score
*_shortest.csv	Nodes ranked by shortest distance
*_fc.csv	Flow centrality nodes
Biological Interpretation

Network proximity provides a quantitative way to evaluate the therapeutic relevance of herbal targets:

Low SAB / negative Z-score → herb targets overlap disease modules

Short-distance nodes → potential mediators

High FC nodes → candidate key regulators

These analyses help reveal the network-level mechanisms of herbal medicine in complex diseases.
