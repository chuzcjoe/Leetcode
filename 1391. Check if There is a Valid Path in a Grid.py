class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        res = True
        
        m = len(grid)
        n = len(grid[0])
        
        dic = {1:[[0,-1],[0,1]],
               2:[[-1,0],[1,0]],
               3:[[0,-1],[1,0]],
               4:[[1,0],[0,1]],
               5:[[0,-1],[-1,0]],
               6:[[-1,0],[0,1]]}
        
        visited = set()
        
        def dfs(i,j):
            if i == m -1 and j == n -1:
                return True
            
            visited.add((i,j))
            
            for d in dic[grid[i][j]]:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and [-d[0], -d[1]] in dic[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            
            return False
        
        
        
        return dfs(0,0)