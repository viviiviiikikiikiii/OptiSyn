# OptiSyn
OptiSyn is an interpretable graph convolutional network (GCN) framework for herbal synergy prediction. It integrates traditional Chinese medicine knowledge with multi-target network modeling on a heterogeneous herb–compound–target–disease network to identify candidate herbs and predict synergistic combinations.
Explainable GCN Framework for Herb Compatibility Prediction

This repository provides the implementation of an explainable Graph Convolutional Network (GCN) framework for predicting potential synergistic interactions between traditional Chinese medicine (TCM) herbs.

The framework integrates biological features, pharmacological attributes, and network topology information to model herb compatibility as a supervised edge-level classification problem.

Overview

To model potential synergistic interactions among herbs, we constructed a graph convolutional network (GCN)-based framework.

In this framework:

Nodes represent herbs

Edges represent potential compatibility relationships between herb pairs

Edge labels indicate whether two herbs form a synergistic combination

The learning task is formulated as a binary classification problem on graph edges.

Positive samples consist of herb pairs that:

Co-occur in TCM prescriptions

Are reported as compatible combinations in the literature

Negative samples are randomly generated herb pairs that do not appear in known prescriptions or reported compatibility records.

Graph Representation

The herb interaction network is represented as:

𝐺
=
(
𝑉
,
𝐸
)
G=(V,E)

Where:

V: set of herb nodes

E: candidate herb–herb interactions

Each herb node is associated with a feature vector describing biological and pharmacological characteristics, derived from herb–target–disease relationships and network topology metrics.

Node features include:

Network topology metrics

dab

Sab

max.diameter

Chemical and pharmacological indicators

average compound effectiveness number (Ec)

overlap rate

Hscore

Mscore

average silhouette score

Drug and disease associations

drug–drug associations

drug–disease associations

Compound characteristics

docking capability

compound efficacy score

Node features are organized as a matrix:

𝑋
∈
𝑅
𝑁
×
𝐹
X∈R
N×F

Where:

N = number of herb nodes

F = feature dimension

All global network features were computed before dataset splitting to avoid information leakage.

Model Architecture

The proposed model is an Explainable Graph Convolutional Network (ExplainableGCN) implemented with PyTorch and PyTorch Geometric.

The architecture includes:

GCN Layer 1

GCN Layer 2

ReLU activation

Dropout layer

Batch normalization

Node embeddings are generated through stacked GCN layers.

For each herb pair, the interaction score is computed as:

𝑠
𝑐
𝑜
𝑟
𝑒
𝑖
𝑗
=
ℎ
𝑖
𝑇
ℎ
𝑗
score
ij
	​

=h
i
T
	​

h
j
	​


where:

ℎ
𝑖
h
i
	​

 and 
ℎ
𝑗
h
j
	​

 are node embeddings.

The score is then converted into probability using a sigmoid activation function.

Model Training

The model is trained by minimizing binary cross-entropy loss between predicted probabilities and ground-truth labels.

Key hyperparameters include:

Hidden layer dimension: 16–128

Learning rate: 1e-2 – 1e-5

Dropout rate: 0–0.6

Training epochs

Hyperparameters are optimized using:

Grid search

Early stopping

Dataset splitting:

Training set: 70%

Testing set: 30%

3-fold cross-validation

All experiments are repeated with multiple random seeds to ensure robustness.

Feature Reduction via SVD

To reduce feature redundancy, Singular Value Decomposition (SVD) is applied to normalized feature matrices.

SVD extracts principal components and allows calculation of pairwise herb correlation coefficients.

These correlations integrate:

intrinsic herb properties

regulatory relationships to disease targets

compound associations

Herbs predicted by the GCN model are further ranked using:

GCN Degree

Average Drug Association scores

Repository Structure
├── explainable_gcn_herb_prediction.py
├── generate_herb_edge_index.py
├── SVD idex.py
├── loss.py
├── features.txt
├── edges.txt
├── labels.txt
└── README.md
File Description
explainable_gcn_herb_prediction.py

Main implementation of the ExplainableGCN model.

Functions include:

GCN model construction

node embedding learning

herb pair interaction scoring

edge-level prediction

training loop implementation

generate_herb_edge_index.py

Generates graph edge indices from herb compatibility matrices.

Output:

edge_index.txt

Used to construct graph structure for GCN training.

SVD idex.py

Performs Singular Value Decomposition (SVD) on multiple feature matrices.

Functions include:

feature normalization

principal component extraction

herb synergy index calculation

pairwise feature correlation analysis

loss.py

Visualization script for training loss curves across epochs.

Produces plots showing model convergence during training.

Example Data Format
Node Features
features.txt

Each row corresponds to a herb node and contains feature values:

0.12 0.33 0.44 0.56 ...
0.22 0.61 0.41 0.88 ...
Edge Index
edges.txt

Each row represents an edge between two herb nodes:

0 5
1 3
4 9
Edge Labels
labels.txt

Binary labels for herb compatibility:

1
0
1
0
Installation

Install required dependencies:

pip install torch
pip install torch-geometric
pip install numpy
pip install matplotlib
pip install networkx
pip install pandas
Running the Model

Run the main training script:

python explainable_gcn_herb_prediction.py

The script will:

Load node features and edge indices

Train the ExplainableGCN model

Predict herb compatibility relationships

Output predicted herb pair interactions

Example Output
Herb A and Herb B: Compatible (Prediction: 1)
Herb C and Herb D: Not Compatible (Prediction: 0)
Visualization

To visualize the loss curve:

python loss.py
Citation

If you use this code in your research, please cite the corresponding study.

License

This project is provided for academic research purposes only.
