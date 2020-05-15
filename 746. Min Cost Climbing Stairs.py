class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, len(cost)+1):
            if i-1 >=0 :
                dp[i] = dp[i-1] + cost[i-1]
            if i-2 >=0:
                dp[i] = min(dp[i-2]+cost[i-2], dp[i])
        
        return dp[len(cost)]
        