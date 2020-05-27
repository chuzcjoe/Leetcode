class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        # dp[i][j] -> number of scores the first player can get more than the second player can get
        
        n = len(nums)
        
        dp = [[-1] * n for i in range(n)]
        
        for i in range(n): dp[i][i] = nums[i]
        for d in range(1,n):
            for i in range(n-d):
                dp[i][i+d] = max(nums[i]-dp[i+1][i+d], nums[i+d]-dp[i][i+d-1])
        
        return dp[0][-1] >= 0