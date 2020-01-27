class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        r = len(grid)
        c = len(grid[0])
        MAX = [[0]*c for _ in range(r)]
        
        def dfs(row,col):
            if 0 <= row <r and 0 <= col <c and grid[row][col]:
                grid[row][col] = 0
                return 1 + dfs(row-1,col) + dfs(row+1,col) + dfs(row, col-1) + dfs(row, col+1)
            
            return 0
            
            
        for i in range(r):
            for j in range(c):
                MAX[i][j] = dfs(i,j)
        
        return max([MAX[i][j] for i in range(r) for j in range(c)])
                
        