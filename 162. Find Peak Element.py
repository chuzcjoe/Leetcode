class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo+hi) // 2
            
            if nums[mid] <= nums[mid+1]:
                lo = mid + 1
            elif nums[mid] <= nums[mid-1]:
                hi = mid - 1
            else:
                return mid
        
        return lo