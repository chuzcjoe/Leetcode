class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        dp = {}
        
        #min cost for painting house[i:] with t different neighbors and house[i-1] is painted as color p
        
        @functools.lru_cache(None)
        def dfs(i,t,p):
            
            key = (i,t,p)
            
            if i == len(houses) or t < 0:
                return 0 if t == 0 else float('inf')
            
            if key not in dp:
                
                if houses[i] == 0:
                    dp[key] = min(dfs(i+1, t-(p != nc), nc) + cost[i][nc-1] for nc in range(1,n+1))
                
                else:
                    
                    dp[key] = dfs(i+1, t-(p != houses[i]), houses[i])
            
            return dp[key]
        
        res = dfs(0,target,-1)
        
        return res if res != float('inf') else -1 