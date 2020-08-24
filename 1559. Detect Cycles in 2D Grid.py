class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        ALL = set()
        seen = set()
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                ALL.add((i,j))
        
        deque = collections.deque([(0,0,None,None)])
        seen.add((0,0))
        
        while ALL:
            size = len(deque)
            if size == 0 :
                seen = set()
                x,y = ALL.pop()
                print(x,y)
                deque.append((x,y,None,None))
                seen.add((x,y))
            
            
            for _ in range(size):
                x,y,px,py = deque.popleft()
                if (x,y) in ALL:
                    ALL.remove((x,y))
                ID = grid[x][y]
                
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) != (px,py) and grid[nx][ny] == ID:
                        deque.append((nx,ny,x,y))
                        if (nx,ny) in seen:
                            return True
                        seen.add((nx,ny))
        
        return False
                    
                        