class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        Solution 1: DP
        
        sum = 0
        for n in nums:
            sum += n
        
        if sum&1:
            return False
        
        sum //= 2
        
        #dp[i][j] means if the first i numbers could add up to j
        dp = [[False]*(sum+1) for i in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1,len(nums)):
            for j in range(1,sum+1):
                #we can either pick nums[i] or don't pick nums[i]
                dp[i][j] = dp[i-1][j]
                if j-nums[i] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        
        return dp[len(nums)-1][sum]
        """
        
        """
        Solution 2: set
        """
        target = 0
        for n in nums:
            target += n
        
        if target&1:
            return False
        
        target //= 2
        
        sum = {0}
        
        for n in nums:
            tmp = set()
            for s in sum:
                if s+n == target:
                    return True
                if s+n < target:
                    tmp.add(s+n)
            sum.update(tmp)
        return False
            