# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
AI-Assisted Discovery of Synergistic Traditional Chinese Medicine Herb Combinations

This repository provides a computational pipeline for predicting potential synergistic combinations of Traditional Chinese Medicine (TCM) herbs for disease treatment.

The framework integrates:

Network pharmacology

Clinical compatibility evidence

Compound structural similarity

Graph neural networks (GCN)

Singular Value Decomposition (SVD)

to systematically identify candidate herb combinations with therapeutic potential.

The complete workflow is divided into six sequential modules, each implemented in a separate GitHub branch.

Graphical Workflow
Raw TCM Data
     │
     ▼
Step 1
Data Preprocessing
     │
     ▼
Step 2
Target–Herb Association Scoring
     │
     ▼
Step 3
Disease–Protein Network Proximity Analysis
     │
     ▼
Step 4
Clinical Herb Co-Usage Profiling
     │
     ▼
Step 5
Compound Structural Similarity Clustering
     │
     ▼
Step 6
GCN-Based Herb Synergy Prediction
     │
     ▼
Predicted Therapeutic Herb Combinations
Pipeline Overview

The proposed framework identifies potential herb combinations through multi-level biological and pharmacological feature integration.

Key components include:

Herb–compound–target associations

Disease-related protein interaction networks

Clinical herb co-occurrence patterns

Compound structural similarity

Graph convolutional neural networks

These heterogeneous features are integrated to predict herb compatibility relationships.

Workflow Modules

The pipeline consists of six major modules.

Each module corresponds to a GitHub branch containing:

compressed datasets

analysis scripts

detailed operation manuals

Step 1 — Preprocessing of Traditional Chinese Medicine–Derived Data

This module prepares the foundational dataset for the entire pipeline.

Data sources include:

TCM databases

compound–target databases

disease-related gene datasets

Processing tasks include:

herb–compound mapping

compound–target integration

disease target collection

data normalization and formatting

The processed dataset provides the input for downstream pharmacological analysis.

Step 2 — Target–Herb Initial Association Assessment

Potential relationships between herbs and disease-related targets are evaluated using two key metrics:

Target Overlap Rate

Measures the overlap between:

herb-associated targets

disease-associated targets

Quantifies the pharmacological potential of compounds linked to herbs.

These indicators provide an initial estimate of herb–disease relevance.

Step 3 — Network Proximity Analysis within the Disease–Protein Interaction Module

This module evaluates the topological relationship between herb targets and disease proteins within a protein–protein interaction network.

Key network metrics include:

dab — average shortest path distance

Sab — separation score between herb targets and disease module

max.diameter — maximum distance within the network

These measures determine the network proximity between herbs and disease modules.

Step 4 — Clinical Co-Usage Profiling and Empirical Herb Association Scoring

Clinical prescription datasets and literature evidence are analyzed to quantify empirical compatibility patterns between herbs.

Key indicators include:

Hscore

Mscore

prescription co-occurrence frequency

These metrics capture real-world clinical usage patterns of TCM herbs.

Step 5 — Structure-Based Similarity Clustering for Key Compound Selection

Compound structural similarity is used to identify representative bioactive compounds.

Main steps include:

molecular structure similarity analysis

clustering of compound structures

selection of key compounds

This step extracts chemical descriptors that contribute to herb pharmacological effects.

Step 6 — Graph Convolutional Network-Based Herb Synergy Prediction

The final step integrates all features into a Graph Convolutional Network (GCN) framework.

Herbs are represented as nodes in a graph, while herb compatibility relationships are modeled as edges.

Node features incorporate:

pharmacological indicators

network topology metrics

compound properties

clinical association scores

To reduce feature redundancy and enhance representation learning, Singular Value Decomposition (SVD) is applied to optimized feature matrices.

The model predicts whether two herbs form a synergistic therapeutic combination.

Repository Structure
TCM-Herb-Synergy-Prediction
│
├── branch1_preprocessing
│
├── branch2_target_herb_association
│
├── branch3_network_proximity
│
├── branch4_clinical_co_usage
│
├── branch5_structure_similarity
│
└── branch6_gcn_synergy_prediction

Each branch includes:

compressed datasets

scripts

operation manuals

Reproducibility

To reproduce the complete workflow:

1 Clone the repository
git clone https://github.com/your_repository_name.git
2 Execute modules sequentially

Start from Branch 1 and proceed to Branch 6.

Example:

git checkout branch1_preprocessing

Follow the instructions in the operation manual provided within the branch.

Expected Outputs

After completing the full pipeline, the framework generates:

predicted herb compatibility relationships

candidate synergistic herb pairs

potential multi-herb therapeutic combinations

These results can support:

TCM compatibility studies

network pharmacology research

AI-assisted drug discovery

Applications

The framework can be applied to:

discovery of novel TCM herb combinations

network pharmacology analysis

multi-component drug design

AI-assisted traditional medicine research

Citation

If you use this framework in your research, please cite the corresponding study.

License

This repository is provided for academic research purposes only.
