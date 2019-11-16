class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = '*'
        
        for r in range(m):
            for c in range(n):
                if dp[r][c] == '*':
                    continue
                if r-1 >= 0 and dp[r-1][c] != '*':
                    dp[r][c] += dp[r-1][c]
                if c - 1 >= 0 and dp[r][c-1] != '*':
                    dp[r][c] += dp[r][c-1]
                    
        
        return dp[m-1][n-1]
