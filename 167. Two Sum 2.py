class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left]+nums[right] > target:
                right -= 1
            else:
                return [left+1,right+1]
        