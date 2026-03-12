import os
os.getcwd()
os.chdir("D:/R/test/")
from numpy.linalg import svd
import numpy as np
# 定义读取矩阵数据的函数
def read_matrix_from_txt(file_path):
    # 从txt文件读取矩阵数据
    with open(file_path, 'r') as file:
        matrix = [list(map(float, line.strip().split())) for line in file]
    return np.array(matrix)
# 指定txt文件路径
file_path_a = 'matrix_a.txt'
# 读取矩阵
matrix_a = read_matrix_from_txt(file_path_a)
# 指定txt文件路径
file_path_b = 'matrix_b.txt'
# 读取矩阵
matrix_b = read_matrix_from_txt(file_path_b)
# 指定txt文件路径
file_path_c = 'matrix_c.txt'
# 读取矩阵
matrix_c = read_matrix_from_txt(file_path_c)
# 指定txt文件路径
file_path_d = 'matrix_d.txt'
# 读取矩阵
matrix_d = read_matrix_from_txt(file_path_d)
# 指定txt文件路径
file_path_e = 'matrix_e.txt'
# 读取矩阵
matrix_e = read_matrix_from_txt(file_path_e)
# 指定txt文件路径
file_path_f = 'matrix_f.txt'
# 读取矩阵
matrix_f = read_matrix_from_txt(file_path_f)
# 指定txt文件路径
file_path_g = 'matrix_g.txt'
# 读取矩阵
matrix_g = read_matrix_from_txt(file_path_g)
# 指定txt文件路径
file_path_h = 'matrix_h.txt'
# 读取矩阵
matrix_h = read_matrix_from_txt(file_path_h)
# 指定txt文件路径
file_path_i = 'matrix_i.txt'
# 读取矩阵
matrix_i = read_matrix_from_txt(file_path_i)
# 指定txt文件路径
file_path_j = 'matrix_j.txt'
# 读取矩阵
matrix_j = read_matrix_from_txt(file_path_j)
# 指定txt文件路径
file_path_k = 'matrix_k.txt'
# 读取矩阵
matrix_k = read_matrix_from_txt(file_path_k)
# 指定txt文件路径
file_path_l = 'matrix_l.txt'
# 读取矩阵
matrix_l = read_matrix_from_txt(file_path_l)
# 指定txt文件路径
file_path_m = 'matrix_m.txt'
# 读取矩阵
matrix_m = read_matrix_from_txt(file_path_m)
# 指定txt文件路径
file_path_n = 'matrix_n.txt'
# 读取矩阵
matrix_n = read_matrix_from_txt(file_path_n)
# 指定txt文件路径
file_path_o = 'matrix_o.txt'
# 读取矩阵
matrix_o = read_matrix_from_txt(file_path_o)
# 指定txt文件路径
file_path_p = 'matrix_p.txt'
# 读取矩阵
matrix_p = read_matrix_from_txt(file_path_p)
# 指定txt文件路径
file_path_q = 'matrix_q.txt'
# 读取矩阵
matrix_q = read_matrix_from_txt(file_path_q)
# 指定txt文件路径
file_path_r = 'matrix_r.txt'
# 读取矩阵
matrix_r = read_matrix_from_txt(file_path_r)
# 指定txt文件路径
file_path_s = 'matrix_s.txt'
# 读取矩阵
matrix_s = read_matrix_from_txt(file_path_s)
# 指定txt文件路径
file_path_t = 'matrix_t.txt'
# 读取矩阵
matrix_t = read_matrix_from_txt(file_path_t)
# 指定txt文件路径
file_path_u = 'matrix_u.txt'
# 读取矩阵
matrix_u = read_matrix_from_txt(file_path_u)
# 指定txt文件路径
file_path_v = 'matrix_v.txt'
# 读取矩阵
matrix_v = read_matrix_from_txt(file_path_v)
# 指定txt文件路径
file_path_w = 'matrix_w.txt'
# 读取矩阵
matrix_w = read_matrix_from_txt(file_path_w)
# 指定txt文件路径
file_path_x = 'matrix_x.txt'
# 读取矩阵
matrix_x = read_matrix_from_txt(file_path_x)

#标准化矩阵
matrix_a_normalized =(matrix_a-matrix_a.mean())/ matrix_a.std()
matrix_b_normalized =(matrix_b-matrix_b.mean())/ matrix_b.std()
matrix_c_normalized =(matrix_c-matrix_c.mean())/ matrix_c.std()
matrix_d_normalized =(matrix_d-matrix_d.mean())/ matrix_d.std()
matrix_e_normalized =(matrix_e-matrix_e.mean())/ matrix_e.std()
matrix_f_normalized =(matrix_f-matrix_f.mean())/ matrix_f.std()
matrix_g_normalized =(matrix_g-matrix_g.mean())/ matrix_g.std()
matrix_h_normalized =(matrix_h-matrix_h.mean())/ matrix_h.std()
matrix_i_normalized =(matrix_i-matrix_i.mean())/ matrix_i.std()
matrix_j_normalized =(matrix_j-matrix_j.mean())/ matrix_j.std()
matrix_k_normalized =(matrix_k-matrix_k.mean())/ matrix_k.std()
matrix_l_normalized =(matrix_l-matrix_l.mean())/ matrix_l.std()
matrix_m_normalized =(matrix_m-matrix_m.mean())/ matrix_m.std()
matrix_n_normalized =(matrix_n-matrix_n.mean())/ matrix_n.std()
matrix_o_normalized =(matrix_o-matrix_o.mean())/ matrix_o.std()
matrix_p_normalized =(matrix_p-matrix_p.mean())/ matrix_p.std()
matrix_q_normalized =(matrix_q-matrix_q.mean())/ matrix_q.std()
matrix_r_normalized =(matrix_r-matrix_r.mean())/ matrix_r.std()
matrix_s_normalized =(matrix_s-matrix_s.mean())/ matrix_s.std()
matrix_t_normalized =(matrix_t-matrix_t.mean())/ matrix_t.std()
matrix_u_normalized =(matrix_u-matrix_u.mean())/ matrix_u.std()
matrix_v_normalized =(matrix_v-matrix_v.mean())/ matrix_v.std()
matrix_w_normalized =(matrix_w-matrix_w.mean())/ matrix_w.std()
matrix_x_normalized =(matrix_x-matrix_x.mean())/ matrix_x.std()

#应用SVD分解得到矩阵A和矩阵B的主成分
_,_,v_a= svd(matrix_a_normalized)
_,_,v_b= svd(matrix_b_normalized)
_,_,v_c= svd(matrix_c_normalized)
_,_,v_d= svd(matrix_d_normalized)
_,_,v_e= svd(matrix_e_normalized)
_,_,v_f= svd(matrix_f_normalized)
_,_,v_g= svd(matrix_g_normalized)
_,_,v_h= svd(matrix_h_normalized)
_,_,v_i= svd(matrix_i_normalized)
_,_,v_j= svd(matrix_j_normalized)
_,_,v_k= svd(matrix_k_normalized)
_,_,v_l= svd(matrix_l_normalized)
_,_,v_m= svd(matrix_m_normalized)
_,_,v_n= svd(matrix_n_normalized)
_,_,v_o= svd(matrix_o_normalized)
_,_,v_p= svd(matrix_p_normalized)
_,_,v_q= svd(matrix_q_normalized)
_,_,v_r= svd(matrix_r_normalized)
_,_,v_s= svd(matrix_s_normalized)
_,_,v_t= svd(matrix_t_normalized)
_,_,v_u= svd(matrix_u_normalized)
_,_,v_v= svd(matrix_v_normalized)
_,_,v_w= svd(matrix_w_normalized)
_,_,v_x= svd(matrix_x_normalized)


synergy_index= np.dot(v_a[0],v_g[0])
print("synergy Index:",synergy_index)


#神奇的偷懒版本
import os
from numpy.linalg import svd
import numpy as np

# 定义读取矩阵数据的函数
def read_matrix_from_txt(file_path):
    # 从txt文件读取矩阵数据
    with open(file_path, 'r') as file:
        matrix = [list(map(float, line.strip().split())) for line in file]
    return np.array(matrix)

# 指定txt文件路径列表
file_paths = [
    'matrix_a.txt', 'matrix_b.txt', 'matrix_c.txt', 'matrix_d.txt',
    'matrix_e.txt', 'matrix_f.txt', 'matrix_g.txt', 'matrix_h.txt',
    'matrix_i.txt', 'matrix_j.txt', 'matrix_k.txt', 'matrix_l.txt',
    'matrix_m.txt', 'matrix_n.txt', 'matrix_o.txt', 'matrix_p.txt',
    'matrix_q.txt', 'matrix_r.txt', 'matrix_s.txt', 'matrix_t.txt',
    'matrix_u.txt', 'matrix_v.txt', 'matrix_w.txt', 'matrix_x.txt'
]

# 读取所有矩阵并标准化
matrices_normalized = []
for file_path in file_paths:
    matrix = read_matrix_from_txt(file_path)
    matrix_normalized = (matrix - matrix.mean()) / matrix.std()
    matrices_normalized.append(matrix_normalized)

# 计算所有矩阵之间的两两 synergy_index 值
num_matrices = len(matrices_normalized)
synergy_indices = {}

for i in range(num_matrices):
    _, _, v_i = svd(matrices_normalized[i])
    for j in range(i + 1, num_matrices):
        _, _, v_j = svd(matrices_normalized[j])
        synergy_index = np.dot(v_i[0], v_j[0])
        synergy_indices[(file_paths[i], file_paths[j])] = synergy_index

# 打印所有 synergy_index 值
for (file_path_1, file_path_2), synergy_index in synergy_indices.items():
    print(f"Synergy Index between {file_path_1} and {file_path_2}: {synergy_index}")
