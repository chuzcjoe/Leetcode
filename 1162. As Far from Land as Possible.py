class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        que = []
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    que.append([i,j])
                    
        que = collections.deque(que)
        
        step = 0
        
        while que:
            size = len(que)
            
            for _ in range(size):
                x,y = que.popleft()
                
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        que.append([nx,ny])
            
            step += 1
            
        
        return -1 if step-1 == 0 else step-1