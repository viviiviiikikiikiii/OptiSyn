# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
Molecular Fingerprint Clustering for Herbal Compounds

This repository contains scripts used to analyze the chemical similarity and clustering patterns of representative compounds from medicinal herbs.

The workflow generates molecular fingerprints, computes Tanimoto similarity, performs K-means clustering, and evaluates clustering quality using Dunn index and silhouette scores.

These results are subsequently integrated to construct a multi-layer network linking disease, herbs, compounds, targets, and pathways.

Method Overview

Representative compounds from medicinal herbs were structurally characterized using molecular fingerprint analysis.

Molecular fingerprints were generated using the R packages:

rcdk

ChemmineR

cluster

Chemical similarity between compounds was quantified using the Tanimoto coefficient, a widely used similarity metric in drug discovery.

Based on pairwise distance matrices derived from fingerprint similarity, K-means clustering was applied to group compounds belonging to the same herb.

The clustering quality was evaluated using:

Dunn Index

Silhouette Score

An average silhouette score ≥ 0.5 was considered acceptable for robust clustering.

Finally, clustering results were integrated into a multi-layer network structure describing:

Disease → Herb → Compound → Target → Pathway
Repository Structure
.
├── batch_mol2_to_sdf.R
├── rcdk.R
└── compound_data/
Workflow

The analysis consists of three main steps.

Step 1. Molecular File Format Conversion

Script:

batch_mol2_to_sdf.R

Many chemical databases provide compound structures in MOL2 format, whereas R cheminformatics tools often require SDF format.

This script converts all MOL2 files in a directory into SDF format using Open Babel.

Input
input_dir/
   compound1.mol2
   compound2.mol2
   compound3.mol2
Output
output_dir/
   compound1.sdf
   compound2.sdf
   compound3.sdf
Example command

The script internally calls:

obabel input.mol2 -O output.sdf
Step 2. Molecular Descriptor and Fingerprint Calculation

Script:

rcdk.R

This step computes molecular descriptors and fingerprints for herbal compounds.

The following properties are extracted:

atom information

bond information

2D molecular coordinates

molecular descriptors

physicochemical properties

Example descriptors include:

Topological Polar Surface Area (TPSA)

XlogP

AlogP

total molecular charge

Step 3. Molecular Fingerprint Similarity Analysis

Molecular fingerprints are generated using:

get.fingerprint(type = "extended")

Other supported fingerprints include:

MACCS fingerprints

Pairwise compound similarity is calculated using the Tanimoto coefficient:

Similarity = Tanimoto(fp1, fp2)

A fingerprint similarity matrix is constructed and converted to a distance matrix:

distance = 1 − similarity
Step 4. Compound Clustering

Clustering analysis is performed using K-means clustering.

The optimal number of clusters is evaluated using:

Within-cluster sum of squares (WSS)

Gap statistic

NbClust package

Example:

k = 3 clusters

This groups compounds within each herb based on structural similarity.

Step 5. Cluster Quality Evaluation

Clustering performance is assessed using two metrics.

Silhouette Score

Measures how similar each compound is to its own cluster compared with other clusters.

silhouette(cluster, distance_matrix)

Interpretation:

Score	Meaning
>0.7	strong clustering
0.5–0.7	reasonable clustering
<0.5	weak clustering

In this study:

Average silhouette ≥ 0.5

was used as the acceptance threshold.

Dunn Index

The Dunn index evaluates:

inter-cluster separation

intra-cluster compactness

Higher Dunn values indicate better cluster quality.

Visualization

Cluster results can be visualized using:

fviz_cluster()

Silhouette plots:

plot(sil)

Hierarchical clustering can also be explored using:

hclust(method = "ward.D2")
Requirements

R packages:

rcdk
ChemmineR
cluster
factoextra
NbClust
fingerprint
fmcsR
ggplot2
vegan
fpc

Install packages:

install.packages("cluster")
install.packages("factoextra")
install.packages("NbClust")
install.packages("ggplot2")

Bioconductor packages:

ChemmineR
fmcsR
Running the Workflow

Example pipeline:

Rscript batch_mol2_to_sdf.R
Rscript rcdk.R
Output

Main outputs include:

File	Description
.sdf files	converted compound structures
fingerprint matrix	molecular fingerprints
similarity matrix	Tanimoto similarity
clustering results	K-means clusters
silhouette plot	cluster validation
Biological Interpretation

The clustering results help identify representative chemical scaffolds within each herb.

These representative compounds are subsequently used to build a multi-layer network model:

Disease
   ↓
Herb
   ↓
Compound
   ↓
Target
   ↓
Pathway

This network framework enables systematic investigation of the multi-component and multi-target mechanisms of herbal medicines.
