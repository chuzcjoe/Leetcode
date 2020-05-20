class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        #dp[i][j] throw i dice get sum j
        
        dp = [[0] * (target+1) for _ in range(d+1)]
        for t in range(1,target+1):
            if t > f:
                break
            dp[1][t] = 1
        
        for i in range(2,d+1):
            for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][j-k] for k in range(1,f+1) if j-k>=0)
        
        print(dp)
        return dp[d][target] % (10**9+7)
        