class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        #dp[i] the max points we can get from first i numbers
        
        if not nums:
            return 0
        
        count = collections.Counter(nums)
        n = max(count.keys())
        res = [0] * (n+1)
        
        for k,v in count.items():
            res[k] = k*v
            
        dp = [0] * len(res)
        dp[0] = res[0]
        
        for i in range(1,len(res)):
            if i == 1:
                dp[i] = max(dp[i-1],res[i])
            else:
                dp[i] = max(dp[i-2]+res[i], dp[i-1])
        
        return dp[n]