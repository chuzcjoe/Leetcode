class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        dp = [-float("inf")] * len(stoneValue)
        
        for i in range(len(stoneValue)-1, -1 ,-1):
            dp[i] = max(dp[i], sum(stoneValue[i:i+1]) - (dp[i+1] if i+1 < len(stoneValue) else 0))
            dp[i] = max(dp[i], sum(stoneValue[i:i+2]) - (dp[i+2] if i+2 < len(stoneValue) else 0))
            dp[i] = max(dp[i], sum(stoneValue[i:i+3]) - (dp[i+3] if i+3 < len(stoneValue) else 0))
        
        if dp[i] == 0:
            return 'Tie'
        elif dp[i] > 0:
            return 'Alice'
        else:
            return 'Bob'