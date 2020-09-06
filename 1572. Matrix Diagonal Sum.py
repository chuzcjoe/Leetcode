class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s = 0
        n = len(mat)
        
        for i in range(n):
            s += mat[i][i]
        
        for j in range(n):
            s += mat[j][n-1-j]
        
        if n % 2:
            return s-mat[n//2][n//2]
        else:
            return s