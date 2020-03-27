class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,-1],[-1,0],[-1,1],
                     [0,-1],[0,1],
                     [1,-1],[1,0],[1,1]]
        
        visited = set()
        cur_nodes = []
        step = 0
        N = len(grid)
        
        visited.add((0,0))
        cur_nodes.append((0,0))
        
        if grid[0][0] == 1:
            return -1
        
        if grid[0][0] == 0 and N == 1:
            return 1
        
        while cur_nodes:
            step += 1
            
            size = len(cur_nodes)
            
            for i in range(size):
                x,y = cur_nodes.pop(0)
                
                for r,c in directions:
                    next_x, next_y = x+r, y+c
                    
                    if 0 <= next_x < N and 0 <= next_y < N and (next_x, next_y) not in visited:
                        if grid[next_x][next_y] == 0:
                            if next_x == N-1 and next_y == N-1:
                                return step+1
                            else:
                                cur_nodes.append((next_x, next_y))
                                visited.add((next_x, next_y))
                    else:
                        continue
        
        return -1