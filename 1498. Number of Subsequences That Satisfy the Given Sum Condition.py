class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        left = 0 
        right = len(nums) - 1
        res = 0
        
        while left <= right:
            if nums[left]+nums[right] > target:
                right -= 1
            
            else:
                res += 2**(right-left)
                left += 1
        
        return res % (10**9+7)
            
            
            
                    