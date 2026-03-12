
#构建邻接矩阵
adjacencyMatrix<-function(pages){
  n<-max(apply(pages,2,max))
  A <- matrix(0,n,n)
  for(i in 1:nrow(pages)) A[pages[i,]$dist,pages[i,]$src]<-1
  A
}

#变换概率矩阵,考虑d的情况
dProbabilityMatrix<-function(G,d=0.85){
  cs <- colSums(G)
  cs[cs==0] <- 1
  n <- nrow(G)
  delta <- (1-d)/n
  A <- matrix(delta,nrow(G),ncol(G))
  for (i in 1:n) A[i,] <- A[i,] + d*G[i,]/cs
  A
}

#直接计算矩阵特征值
calcEigenMatrix<-function(G){
  x <- Re(eigen(G)$vectors[,1])
  x/sum(x)
}
pages<-read.table(file="PR.csv",header=FALSE,sep=",")
names(pages)<-c("src","dist")
A<-adjacencyMatrix(pages)
G<-dProbabilityMatrix(A)
q<-calcEigenMatrix(G)

df<-data.frame(Object=1:length(q),PageRank=q)
