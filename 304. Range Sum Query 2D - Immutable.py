class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if matrix and matrix[0]:
            self.r = len(matrix)
            self.c = len(matrix[0])
            self.dp = [[0]*(self.c+1) for _ in range(self.r+1)]
            self.dp[self.r-1][self.c-1] = matrix[self.r-1][self.c-1] 
        
            for i in range(self.r-1,-1,-1):
                for j in range(self.c-1,-1,-1):
                    self.dp[i][j] = matrix[i][j] + self.dp[i][j+1] + self.dp[i+1][j] - self.dp[i+1][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.dp[row1][col1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row2+1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)