class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
    
        dp = [-1] * (target+1)
        dp[0] = 0
        
        for t in range(1, target+1):
            dp[t] = max([dp[t-c]*10+i+1 for i,c in enumerate(cost) if t-c >= 0] or [-1])
        
        return '0' if dp[target] < 0 else str(dp[target])
            
        