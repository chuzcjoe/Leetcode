class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        # find the rotated index
        
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] >= nums[hi]:
                if len(set(nums[mid:])) == 1:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                hi = mid
        
        # lo == hi : smallest number index
        
        rotate = lo
        
        
        lo = 0
        hi = rotate-1
        print(lo,hi)
        
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        lo = rotate
        hi = len(nums) -1
        print(lo,hi)
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        
        return False