class Solution:
    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def dp(i, gas):
            if gas < abs(loc[i]-loc[finish]):
                return 0
            
            ans = 0
            if i == finish:
                ans += 1
                
            for nxt in range(len(loc)):
                if nxt != i:
                    ans += dp(nxt, gas-abs(loc[i]-loc[nxt]))
            
            return ans
        
        res = dp(start, fuel)
        
        return res % (10**9+7)
            
            
            
            
            
            
        