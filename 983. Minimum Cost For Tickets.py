class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0] * 366
        
        for i in range(1,366):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
            
            if i == days[-1]:
                return dp[i]