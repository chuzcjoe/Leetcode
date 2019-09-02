class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp = [0 for i in range(0,target+1)]
        dp[0] = 1
        
        for i in range(1, target+1):
            for val in nums:
                if i >= val:
                    dp[i] += dp[i-val]
        #print(dp)      
        return dp.pop()