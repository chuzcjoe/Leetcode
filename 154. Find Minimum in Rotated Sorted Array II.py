class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
         # find the rotated index
        
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] >= nums[hi]:
                if len(set(nums[mid:hi+1])) == 1:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                hi = mid
            
            
        
        # lo == hi : smallest number index
        
        rotate = lo
        
        return nums[rotate]

        