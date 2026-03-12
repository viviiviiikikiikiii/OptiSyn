# 定义批量转换函数
convert_mol2_to_sdf <- function(input_dir, output_dir) {
  # 创建输出目录（如果不存在）
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)
  }
  
  # 获取所有 mol2 文件
  mol2_files <- list.files(input_dir, pattern = "\\.mol2$", full.names = TRUE)
  
  # 遍历每个文件并调用 Open Babel
  for (mol2_file in mol2_files) {
    # 获取文件名（无扩展名）
    file_name <- tools::file_path_sans_ext(basename(mol2_file))
    
    # 定义输出文件路径
    sdf_file <- file.path(output_dir, paste0(file_name, ".sdf"))
    
    # 构造 Open Babel 命令
    command <- sprintf("obabel %s -O %s", shQuote(mol2_file), shQuote(sdf_file))
    
    # 执行命令
    system(command)
    
    # 打印转换信息
    cat("Converted:", mol2_file, "to", sdf_file, "\n")
  }
}

# 设置输入和输出目录
input_dir <- "D:/R/SDF"  # 替换为你的 mol2 文件目录
output_dir <- "D:/R/SDF"  # 替换为目标输出目录

# 执行批量转换
convert_mol2_to_sdf(input_dir, output_dir)

cat("所有 mol2 文件已成功转换为 sdf 格式！\n")
