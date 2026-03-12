# 读取文本文件
file_path <- "test1223.txt"
data <- readLines(file_path, encoding = "UTF-8")

# 提取处方名称和中药名称
library(stringr)
prescriptions <- str_extract_all(data, "(?<=\\t)[^\\t]+")
prescription_names <- str_extract(data, "处方\\d+")

# 将中药数据整理为数据框
unique_herbs <- unique(unlist(prescriptions))  # 所有唯一中药名称
herb_matrix <- sapply(prescriptions, function(p) unique_herbs %in% p)  # 创建矩阵
herb_matrix <- t(herb_matrix)  # 转置矩阵行为处方

# 添加处方名称作为行名
rownames(herb_matrix) <- prescription_names
colnames(herb_matrix) <- unique_herbs

# 转换为数据框格式
herb_df <- as.data.frame(herb_matrix)
herb_df[herb_df == TRUE] <- 1  # 将 TRUE 转换为 1
herb_df[herb_df == FALSE] <- 0  # 将 FALSE 转换为 0

# 查看结果
print(head(herb_df))

# 保存为 CSV 文件
write.csv(herb_df, "herb_presence_matrix.csv", row.names = TRUE)
