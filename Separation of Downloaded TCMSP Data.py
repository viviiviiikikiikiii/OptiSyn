import pandas as pd

# 指定两个文件路径
file_path1 = r'D:\R\成分靶点数据\Rhododendronmolleingredients.xlsx'
file_path2 = r'D:\R\成分靶点数据\Rhododendronmolletargets.xlsx'

df1 = pd.read_excel(file_path1)
df2 = pd.read_excel(file_path2)

# 筛选表一中满足条件的行
filtered_df = df1[(df1['OB (%)'] >= 30) & (df1['DL'] >= 0.18)]
# 保留所需的列
result_df = filtered_df[['Mol ID', 'OB (%)', 'DL']]
# 打印结果
print("表一中满足条件的行:")
print(result_df)
print("====================================================================================")

# 使用 merge 函数合并两个 DataFrame
merged_df = pd.merge(df2, result_df, on='Mol ID', how='inner')
# 保留所需的列
final_result = merged_df[['Mol ID', 'Target name']]
# 保存最终结果为 Excel 文件
final_result.to_excel(r'F:\GA\今天好好找中药了吗\gene\Final_result-Rhododendronmolle.xlsx', index=False)
# 打印最终结果
print("最终结果:")
print(final_result)