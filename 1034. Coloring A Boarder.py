class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        val = grid[r0][c0]
        
        def dfs(x,y):
            grid[x][y], cnt = -val, 0
            
            for r,c in [[x+1,y],[x-1,y],[x,1+y],[x,y-1]]:
                if m > r >= 0 <= c < n:
                    cnt += abs(grid[r][c]) == val
                    if grid[r][c] == val:
                        dfs(r,c)
            if cnt == 4:
                grid[x][y] = val
        
        
        dfs(r0,c0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -val:
                    grid[i][j] = color
        
        return grid
            
                