class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        # Take exact N step to move out of the boundary
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
        
        for s in range(1, N+1):
            for x in range(m):
                for y in range(n):
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        n_x, n_y = x+dx, y+dy
                        
                        if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n:
                            dp[s][x][y] += 1
                        
                        else:
                            dp[s][x][y] += dp[s-1][n_x][n_y]
        
        return dp[N][i][j] % (10**9+7)
        