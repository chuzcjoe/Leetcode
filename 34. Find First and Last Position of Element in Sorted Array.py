class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lo = 0
        hi = len(nums) - 1
        
        if not nums:
            return [-1,-1]
        
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] < target:
                lo = mid+1 
            else:
                hi = mid
            
        if lo == hi and nums[lo] != target:
            return [-1,-1]
        
        start = lo
        print(start)
        
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        
        end = hi
        print(end)
        
        return [start,end]
        
        