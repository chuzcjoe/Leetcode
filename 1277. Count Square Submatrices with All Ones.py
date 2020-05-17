class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        r = len(matrix)
        c = len(matrix[0])
        side = min(r,c)
        
        dp = [[0] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    if i!=0 and j!=0:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    else:
                        dp[i][j] = 1
        
        return sum(sum(row) for row in dp)        