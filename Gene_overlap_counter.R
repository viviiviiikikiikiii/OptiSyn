# 加载必要的包
library(dplyr)

# 1. 定义目标文件路径
target_file <- "D:\\R\\sab\\tar\\gene0.txt"

# 2. 定义一堆txt文件的文件夹路径
txt_folder <- "D:\\R\\sab\\gene"

# 3. 读取目标基因列表
target_genes <- readLines(target_file)

# 4. 获取文件夹中所有的txt文件
file_list <- list.files(txt_folder, pattern = "\\.txt$", full.names = TRUE)

# 5. 初始化存储结果的数据框
results <- data.frame(
  file_name = character(),
  common_gene_count = numeric(),
  stringsAsFactors = FALSE
)

# 6. 遍历每个文件，计算与目标文件的重复基因个数
for (file in file_list) {
  # 读取当前文件的基因列表
  current_genes <- readLines(file)
  
  # 计算重复的基因个数
  common_genes <- intersect(target_genes, current_genes)
  common_count <- length(common_genes)
  
  # 将结果存入数据框
  results <- results %>%
    add_row(file_name = basename(file), common_gene_count = common_count)
}

# 7. 打印结果
print(results)

# 8. 保存结果到文件（可选）
write.csv(results, "common_genes_results.csv", row.names = FALSE)