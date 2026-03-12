# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
Clinical Experience–Based Pharmacopeia Evaluation

This repository contains the scripts used to evaluate herbal co-administration patterns in clinical practice and to identify representative herbs in therapeutic combination systems.

The workflow integrates clinical experience–derived herbal pair data, target gene overlap analysis, and factor analysis of herb co-occurrence patterns to quantify the empirical relevance of herbs in disease treatment.

Method Overview

A clinical experience–based pharmacopeia evaluation framework was developed to quantitatively characterize the patterns of herbal co-administration in real-world clinical practice.

A total of 28,279 herbal pair combinations were collected from the Chinese Patent Medicine Value Evaluation Information Database. Each herbal pair was systematically retrieved, deduplicated, and standardized.

Two main metrics were used:

Pscore – Empirical Herbal Pair Strength

Pscore reflects the empirical combination patterns accumulated through long-term clinical practice.
It quantifies how frequently a given herbal pair appears in clinical prescriptions.

Higher Pscore values indicate stronger empirical compatibility between herbs.

Mscore – Herb Representativeness

To enhance the clinical relevance of the analysis, all published TCM formula studies related to the target disease (2019–2024) were collected from CNKI.

After data cleaning and normalization:

Herbal pairs and formula datasets were constructed

Herb occurrence frequencies were calculated

Factor analysis was performed on the herb co-occurrence matrix

Mscore measures the representativeness of a herb in the therapeutic co-administration system, defined as the average co-occurrence frequency across frequently used herbal pairs.

Higher Mscore values indicate herbs that are central to the clinical prescription network.

Repository Structure
.
├── apriori_herb_association_rules.R
├── build_herb_presence_matrix.R
├── herb_frequency_analysis.R
├── herb_factor_analysis.R
└── herb_presence_matrix.csv
Workflow

The analysis pipeline consists of four main steps.

Step 1. Herb–Target Overlap Analysis

Script:

apriori_herb_association_rules.R

This script calculates the overlap between herb target genes and disease-associated genes.

Procedure:

Load disease target genes

Read herb target gene lists

Calculate gene intersections

Count overlapping genes

Export results

Output:

common_genes_results.csv

Columns:

Column	Description
file_name	herb gene file
common_gene_count	number of overlapping genes
Step 2. Herb Presence Matrix Construction

Script:

build_herb_presence_matrix.R

This step constructs a herb presence matrix representing herb co-occurrence patterns across formulas.

Each row represents a formula, and each column represents a herb.

Matrix values indicate whether a herb appears in the formula.

Example:

Formula     HerbA   HerbB   HerbC
Formula1      1       0       1
Formula2      1       1       0
Formula3      0       1       1

This matrix serves as the input for frequency analysis and factor analysis.

Step 3. Herb Frequency Analysis

Script:

herb_frequency_analysis.R

This script evaluates herb occurrence frequency within high-occurrence herbal combinations.

Main analyses:

correlation matrix calculation

KMO test

Bartlett’s sphericity test

frequency evaluation

Outputs:

bartlett_result.csv

These statistics confirm whether the dataset is suitable for factor analysis.

Step 4. Herb Factor Analysis

Script:

herb_factor_analysis.R

Factor analysis is used to identify latent herb combination patterns within the dataset.

Steps:

Load herb presence matrix

Compute correlation matrix

Evaluate KMO and Bartlett statistics

Perform factor extraction

Apply Varimax rotation

Parameters used in the study:

nfactors = 15
rotation = varimax

Output:

factor_loadings.csv

This matrix shows the association strength between herbs and latent prescription factors.

Requirements

R packages:

dplyr
psych

Install dependencies:

install.packages("dplyr")
install.packages("psych")
Running the Analysis

Example workflow:

Rscript apriori_herb_association_rules.R
Rscript build_herb_presence_matrix.R
Rscript herb_frequency_analysis.R
Rscript herb_factor_analysis.R
Output Files
File	Description
common_genes_results.csv	Herb–disease gene overlap
herb_presence_matrix.csv	Herb occurrence matrix
bartlett_result.csv	Bartlett test results
factor_loadings.csv	Factor analysis loadings
Interpretation

This framework allows quantitative evaluation of herbal combination patterns derived from clinical experience.

The results provide insights into:

empirical herb compatibility (Pscore)

herb centrality within prescriptions (Mscore)

latent herbal combination structures

representative herbs in disease treatment

These findings help bridge clinical empirical knowledge and computational pharmacology.
