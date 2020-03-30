class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        cur_gold = 0
        max_gold = 0
        
        r, c = len(grid), len(grid[0])
        visited = [[0 for i in range(c)] for j in range(r)]
        
        options = [[-1,0],[1,0],[0,1],[0,-1]]
        
        def backtrack(x, y, r, c, grid):
            
            nonlocal cur_gold, max_gold
            
            if grid[x][y] == 0:
                return
            
            # add to cur_gold amount
            cur_gold += grid[x][y]
            
            # check max
            max_gold = max(max_gold, cur_gold)
            
            # take gold out from cur suqare
            gold_at_cell = grid[x][y]
            grid[x][y] = 0
            
            for i, j in options:
                next_x, next_y = x +i, y+j
                if 0 <= next_x < r and 0 <= next_y < c:
                    backtrack(next_x, next_y, r, c, grid)
            
            cur_gold -= gold_at_cell
            grid[x][y] = gold_at_cell
        
        
        
        def dfs1(x, y, r, c, visited, grid):
            if x < 0 or x >= r or y < 0 or y >= c or visited[x][y] or grid[x][y] == 0:
                return 0
            
            visited[x][y] = 1
            
            left = dfs1(x,y-1,r,c, visited, grid)
            right = dfs1(x,y+1,r,c, visited, grid)
            up = dfs1(x-1,y,r,c, visited, grid)
            down = dfs1(x+1,y,r,c, visited, grid)
            
            visited[x][y] = 0
            
            
            return max(left, right, up, down) + grid[x][y]
        
        
        
        """
         res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    res = max(res, dfs1(i,j,r,c,visited,grid))
        
        return res
        """
        for i in range(r):
            for j in range(c):
                backtrack(i,j, r, c, grid)
        
        return max_gold
                
            
            
            
        