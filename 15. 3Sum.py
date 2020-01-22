class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        results = []
        
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: continue
           
            while l < r:
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    results.append([nums[l],nums[r],nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        
        return results
        