class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        q = []
        start = None
        r = len(grid)
        c = len(grid[0])
        unique_keys = set()
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in 'abcdef':
                    unique_keys.add(grid[i][j])
                if grid[i][j] == "@":
                    start = [i,j]
        
        q.append([start[0],start[1],".@abcdef",0, 0])
        seen.add((start[0],start[1],".@abcdef"))
        
        while q:
            x,y,keys,steps,num_keys = q.pop(0)
            
            if grid[x][y] in 'abcdef' and grid[x][y].upper() not in keys:
                keys += grid[x][y].upper()
                num_keys += 1
            
            if num_keys == len(unique_keys):
                return steps
                
            
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] in keys:    
                    if (nx,ny,keys) not in seen:
                        seen.add((nx,ny,keys))
                        q.append([nx,ny,keys,steps+1,num_keys])
        
        return -1