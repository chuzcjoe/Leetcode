class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        fresh = {(i,j) for i in range(r) for j in range(c) if grid[i][j]==1}
        rotting = {(i,j) for i in range(r) for j in range(c) if grid[i][j]==2}
        
        time = 0
        
        while fresh:
            if not rotting: return -1
            rotting = {(i+dx,j+dy) for i,j in rotting for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]] if (i+dx, j+dy) in fresh}
            fresh -= rotting
            time += 1
        
        return time
        
        
        