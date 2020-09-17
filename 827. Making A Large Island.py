class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        def dfs(i,j,index):
            res = 0
            grid[i][j] = index
            
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx, ny = i+dx, j+dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                    res += dfs(nx,ny,index)
            
            return res + 1
        
        areas = {0:0}
        index = 2
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    area = dfs(i,j,index)
                    areas[index] = area
                    index += 1
        
        max_area = max(areas.values())
        
        for ii in range(r):
            for jj in range(c):
                if grid[ii][jj] == 0:
                    connected = set()
                    
                    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                        nii, njj = ii+dx, jj+dy
                        if 0 <= nii < r and 0 <= njj < c:
                            connected.add(grid[nii][njj])
                    
                    max_area = max(max_area, sum(areas[idx] for idx in connected)+1)
        
        return max_area
        
        
                    
        
                    