# 安装 arules 包（如果未安装）
if (!require("arules")) install.packages("arules")

# 加载 arules 包
library(arules)
# 读取 CSV 文件
file_path <- "herb_presence_matrix.csv"
data <- read.csv(file_path, header = TRUE, row.names = 1, check.names = FALSE)

# 检查数据格式
str(data)
head(data)

# 确保数据为事务格式（转为 logical）
data <- as.data.frame(lapply(data, as.logical))
# 转换为事务数据
transactions <- as(data, "transactions")

# 检查事务数据
summary(transactions)
inspect(head(transactions, 5))  # 查看前 5 条事务
# 应用 apriori 算法
rules <- apriori(
  transactions,
  parameter = list(support = 0.1, confidence = 0.5)
)

# 查看规则数量
summary(rules)
# 按支持度排序规则
rules_sorted <- sort(rules, by = "support", decreasing = TRUE)

# 查看前 10 条规则
inspect(head(rules_sorted, 10))
# 安装 arulesViz 包（如果未安装）
if (!require("arulesViz")) install.packages("arulesViz")

# 加载 arulesViz 包
library(arulesViz)

# 绘制关联规则图
plot(rules_sorted, method = "graph", engine = "htmlwidget")
# 保存规则为 CSV
write(rules_sorted, file = "apriori_rules.csv", sep = ",", quote = TRUE, row.names = FALSE)

