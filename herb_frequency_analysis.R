# 读取文本文件
text_data <- readLines("test1217.txt", encoding = "UTF-8")

# 将所有文本合并为一个字符串
text_combined <- paste(text_data, collapse = " ")

# 分割文本为单个中药名称，使用空格或制表符作为分隔符
herbs <- unlist(strsplit(text_combined, "\\s+"))

# 去除空字符串
herbs <- herbs[herbs != ""]

# 统计每个中药名称的出现次数
herb_counts <- table(herbs)

# 转换为数据框并按次数降序排列
herb_counts_df <- as.data.frame(herb_counts)
colnames(herb_counts_df) <- c("中药名称", "出现次数")
herb_counts_df <- herb_counts_df[order(-herb_counts_df$出现次数), ]

# 打印前10个中药及其出现次数
print(head(herb_counts_df, 10))

# 保存结果到CSV文件
write.csv(herb_counts_df, "herb_counts.csv", row.names = FALSE)
