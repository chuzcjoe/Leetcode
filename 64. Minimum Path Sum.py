class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        
        r = len(grid)
        c = len(grid[0])
        
        
        dp =  [[0]*c for _ in range(r)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(1,c):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1,r):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
        