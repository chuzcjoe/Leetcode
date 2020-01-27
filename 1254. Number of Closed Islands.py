class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        
        if r==1 or c==1:
            return 0
        
        def dfs(row,col,val):
            if 0<= row < r and 0<= col < c and grid[row][col] == 0:
                grid[row][col] = 1
                dfs(row-1,col,val)
                dfs(row+1,col,val)
                dfs(row,col-1,val)
                dfs(row,col+1,val)
        
        for i in range(r):
            for j in range(c):
                if i == 0 or i==r-1 or j ==0 or j == c-1:
                    dfs(i,j,1)
        
        res = 0
        
        for i in range(r):
            for j in range(c):
                if not grid[i][j]:
                    dfs(i,j,1)
                    res += 1
        
        return res
        