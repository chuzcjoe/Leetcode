class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        h = len(grid)
        w = len(grid[0])
        
        
        def bfs(grid,x,y,visited,t):
            visited[x][y] = '*'
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            if grid[x][y] > t:
                return
            
            for d in directions:
                nxt_x = x + d[0]
                nxt_y = y + d[1]
                if nxt_x < 0 or nxt_x >= h or nxt_y < 0 or nxt_y >= w or grid[nxt_x][nxt_y] > t or visited[nxt_x][nxt_y] == '*':
                    continue
                bfs(grid,nxt_x,nxt_y,visited,t)
                
        cnt = grid[0][0] if grid[0][0] > grid[h-1][w-1] else grid[h-1][w-1]
        while 1:
            print(cnt)
            visited = [[0]*w for _ in range(h)]
            bfs(grid,0,0,visited,cnt)
            if visited[h-1][w-1] == '*':
                #print(visited)
                break
            
            cnt += 1
        
        return cnt
            