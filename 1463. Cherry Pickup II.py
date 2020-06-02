class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == m:
                return 0
            
            cherry = grid[r][c1]+grid[r][c2] if c1!=c2 else grid[r][c1]
            
            ans = 0
            
            for rob1 in range(c1-1, c1+2):
                for rob2 in range(c2-1, c2+2):
                    if 0 <= rob1 < n and 0 <= rob2 < n:
                        ans = max(ans, dfs(r+1, rob1, rob2))
            
            return cherry + ans
        
        return dfs(0,0,n-1)
       