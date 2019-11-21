class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)
        cnt = 0
        idx = 0
        
        if not nums:
            return 0
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j] + 1
                        dp2[i] = dp2[j]
                    elif dp1[j] + 1 == dp1[i]:
                        dp2[i] += dp2[j]
                
        MAX = max(dp1)
        for i,x in enumerate(dp1):
            if x == MAX:
                cnt += dp2[i]
        
        return cnt