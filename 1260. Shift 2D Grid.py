class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        r = len(grid)
        c = len(grid[0])
        
        for i in range(k):
            
            col = [row[-1] for row in grid]
            for i in range(r):
                grid[i][1:] = grid[i][:-1]
                if i == 0:
                    grid[0][0] = col[-1]
                else:
                    grid[i][0] = col[i-1]
        
        return grid
            
            
