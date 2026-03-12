import itertools
import os
import os.path as osp
import pickle
import urllib
from collections import namedtuple
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import scipy.sparse as sp
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
import torch.optim as optim
import matplotlib.pyplot as plt
%matplotlib inline
#chatGPT调试
import networkx as nx
import numpy as np
import pandas as pd
import random as rd
import os
os.getcwd()
os.chdir("D:/R/COM/")
import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.data import Data, DataLoader
from torch_geometric.nn import GCNConv
import torch.nn.functional as F

class ExplainableGCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(ExplainableGCN, self).__init__()
        self.gcn1 = GCNConv(input_dim, hidden_dim)# 第一层图卷积
        self.gcn2 = GCNConv(hidden_dim, hidden_dim)# 第二层图卷积
        self.dropout = nn.Dropout(p=0.5)# Dropout 防止过拟合
        self.batch_norm = nn.BatchNorm1d(hidden_dim)# 批归一化
        self.weight_vector = nn.Parameter(torch.empty(hidden_dim))# 可学习权重向量
        nn.init.uniform_(self.weight_vector, -1.0, 1.0)# 初始化权重向量
        self.sigmoid = nn.Sigmoid()# 激活函数，将分数映射为 [0,1]

    def forward(self, x, edge_index):
        # GCN Layers with ReLU activation
        x = self.gcn1(x, edge_index)# 图卷积层 1
        x = F.relu(x)# 激活函数
        x = self.gcn2(x, edge_index)# 图卷积层 2
        x = F.relu(x)# 激活函数

        # Dropout and Batch Normalization
        x = self.dropout(x)
        x = self.batch_norm(x)

        return x

    def calculate_score(self, x, edge_index):
        # 计算节点嵌入
        node_embeddings = self.forward(x, edge_index)

        edge_scores = []
        for i, j in edge_index.t():  # 遍历每一条边
            # 确保 node_embeddings[i] 和 node_embeddings[j] 都是 (hidden_dim,)
            node_i = node_embeddings[i]
            node_j = node_embeddings[j]

            # 使用 torch.matmul 计算节点 i 和节点 j 的内积，确保两个向量的维度是 (hidden_dim,)
            score = torch.matmul(node_i, node_j)  # (hidden_dim,) @ (hidden_dim,) -> scalar
            edge_scores.append(score)

        edge_scores = torch.stack(edge_scores)  # 堆叠为张量
        edge_probs = self.sigmoid(edge_scores)  # 映射为概率
        return edge_probs

    def predict(self, x, edge_index, threshold=0.5):
        edge_probs = self.calculate_score(x, edge_index)# 计算边的概率
        predictions = (edge_probs > threshold).float()# 应用阈值进行二值化
        return predictions

# Example Data Preparation
def generate_example_data():
    """
    Generate an example graph data structure with disease and herb gene nodes.
    Each node represents genes, and edges represent interactions between them.
    """
    num_nodes = 50 # 节点数
    num_features = 16# 节点特征维度
    edge_index = torch.randint(0, num_nodes, (2, 150))  # Randomly generated edges# 随机生成边索引
    x = torch.rand((num_nodes, num_features))  # Randomly generated node features# 随机节点特征
    y = torch.randint(0, 2, (edge_index.size(1),))  # Binary labels for edges# 边标签（0 或 1）
    return Data(x=x, edge_index=edge_index, y=y)

# Training Function
def train(model, data, optimizer, criterion, epochs=50):
    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()# 清空梯度
        edge_probs = model.calculate_score(data.x, data.edge_index)# 计算边的概率
        loss = criterion(edge_probs, data.y.float())# 二元交叉熵损失
        loss.backward()# 反向传播
        optimizer.step() # 更新权重
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# Main Function
import torch
from torch_geometric.data import Data

def load_txt_data(feature_file, edge_file, label_file):
    """
    Load graph data from .txt files.
    Args:
        feature_file: Path to the node feature file.
        edge_file: Path to the edge index file.
        label_file: Path to the edge label file.
    Returns:
        A PyTorch Geometric Data object.
    """
    # 加载节点特征
    x = []
    with open(feature_file, 'r') as f:
        for line in f:
            features = list(map(float, line.strip().split()))
            x.append(features)
    x = torch.tensor(x, dtype=torch.float)

    # 加载边索引
    edge_index = []
    with open(edge_file, 'r') as f:
        for line in f:
            edge = list(map(int, line.strip().split()))
            edge_index.append(edge)
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()

    # 加载边标签
    y = []
    with open(label_file, 'r') as f:
        for line in f:
            label = int(line.strip())
            y.append(label)
    y = torch.tensor(y, dtype=torch.float)

    # 构造 Data 对象
    return Data(x=x, edge_index=edge_index, y=y)

import torch
# 生成20行特征，每行9个维度
num_rows = 24
num_cols = 8
features = torch.rand((num_rows, num_cols))

# 保存到文件
with open("features.txt", "w") as f:
    for row in features:
        f.write(" ".join(map(str, row.tolist())) + "\n")
import torch

# 参数设置
num_nodes = 24  # 节点数
num_edges = 224  # 边数

# 生成 edges.txt
edges = torch.randint(0, num_nodes, (num_edges, 2))
with open("edges.txt", "w") as f:
    for edge in edges:
        f.write(f"{edge[0].item()} {edge[1].item()}\n")

# 生成 labels.txt (对应每条边的标签)
labels = torch.randint(0, 2, (num_edges,))
with open("labels.txt", "w") as f:
    for label in labels:
        f.write(f"{label.item()}\n")

# 带有预测值的主程序
if __name__ == "__main__":
    # 文件路径
    feature_file = "features.txt"
    edge_file = "edges.txt"
    label_file = "labels.txt"

    # 加载数据
    data = load_txt_data(feature_file, edge_file, label_file)

    # 中药节点名称（假设每个节点代表一个中药）
    node_names = [f"中药{i+1}" for i in range(data.x.size(0))]  # 假设有 data.x.size(0) 个中药节点

    # 参数设置
    input_dim = data.x.size(1)
    hidden_dim = 32
    output_dim = 1
    learning_rate = 0.0001
    epochs = 100

    # 初始化模型
    model = ExplainableGCN(input_dim, hidden_dim, output_dim)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.BCELoss()
    #梯度裁剪（Gradient Clipping），防止梯度爆炸导致损失突然升高
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    # 训练模型
    train(model, data, optimizer, criterion, epochs)

    # 测试模型
    model.eval()
    with torch.no_grad():
        predictions = model.predict(data.x, data.edge_index)

        # 输出预测结果
        for i in range(data.edge_index.size(1)):
            node_i = data.edge_index[0, i].item()
            node_j = data.edge_index[1, i].item()
            prediction = predictions[i].item()
            relation = '存在' if prediction == 1 else '不存在'

            print(f"中药 {node_names[node_i]} 和 中药 {node_names[node_j]} 之间的关系: {relation} (预测值: {prediction:.2f})")

