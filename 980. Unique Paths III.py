class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        start = [0,0]
        
        r = len(grid)
        c = len(grid[0])
        zeros = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    zeros += 1
                if grid[i][j] == 1:
                    start = [i,j]
        
        def dfs(i,j,cnt,visited):
            nonlocal res
            
            visited.append([i,j])
            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                x = i+dx
                y = j+dy
                
                if 0 <= x < r and 0 <= y < c:
                    if grid[x][y] == 0 and [x,y] not in visited:
                        dfs(x,y,cnt+1,visited[:])
                        
                    elif grid[x][y] == 2:
                        if cnt == zeros:
                            res += 1
                        else:
                            continue
        
        res = 0
        visited = []
        dfs(start[0],start[1],0,visited)
        return res
            
        
        