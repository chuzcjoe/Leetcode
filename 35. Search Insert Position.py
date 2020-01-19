class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if target <= nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] == target:
                return i
            
            if  nums[i-1] < target < nums[i]:
                return i
            
        