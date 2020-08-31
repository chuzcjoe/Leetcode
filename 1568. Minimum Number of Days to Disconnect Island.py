class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        def dfs(g, i,j):
            if g[i][j] == 0:
                return 
            
            g[i][j] = 0
            
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni,nj = i+dx, j+dy
                if 0 <= ni < r and 0 <= nj < c:
                    dfs(g,ni,nj)
        
        def num_island(g):
            cnt = 0
            for i in range(r):
                for j in range(c):
                    if g[i][j]:
                        cnt += 1
                        dfs(g, i, j)
            
            return cnt
        
        g = copy.deepcopy(grid)
        n = num_island(g)
        
        if n != 1:
            return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    g = copy.deepcopy(grid)
                    g[i][j] = 0
                    if num_island(g) != 1:
                        return 1
        
        return 2
        
        
            
            
            