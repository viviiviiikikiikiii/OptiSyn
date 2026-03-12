# 加载数据
file_path <- "herb_presence_matrix.csv"
data <- read.csv(file_path, header = TRUE, row.names = 1, check.names = FALSE)

# 查看数据结构
str(data)

# 检查前几行
head(data)
library(psych)

# 计算相关矩阵
cor_matrix <- cor(data)

# 检查 KMO 值
kmo_result <- KMO(cor_matrix)
print(kmo_result)

# Bartlett's 球形检验
bartlett_result <- cortest.bartlett(cor_matrix, n = nrow(data))
print(bartlett_result)
write.csv(bartlett_result, "bartlett_result.csv", row.names = TRUE)

# 因子分析（提取3个因子，旋转方式为 Varimax）
fa_result <- fa(data, nfactors = 15, rotate = "varimax")

# 查看因子分析结果
print(fa_result)

# 因子载荷矩阵
print(fa_result$loadings)

# 保存因子载荷矩阵
write.csv(fa_result$loadings, "factor_loadings.csv")

