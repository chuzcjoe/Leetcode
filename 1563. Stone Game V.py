class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        presum = [0]
        s = 0
        n = len(stoneValue)
        for a in stoneValue:
            s += a
            presum.append(s)
        
        @lru_cache(None)
        def dp(i,j):
            if i+1 == j:
                return min(stoneValue[i-1:j])
            
            if i == j:
                return 0
            
            ans = 0
            res = []
            for k in range(i,j):
                if presum[k]-presum[i-1] > presum[j]-presum[k]:
                    ans = presum[j]-presum[k] + dp(k+1,j)
                elif presum[k]-presum[i-1] < presum[j]-presum[k]:
                    ans = presum[k]-presum[i-1] + dp(i,k)
                else:
                    ans = max(dp(i,k),dp(k+1,j)) + presum[j]-presum[k]
                
                res.append(ans)
            
            return max(res)
        
        return dp(1,n)
                
                
                
                