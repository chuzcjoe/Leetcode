class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        res = 0
        zero_cnt = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            
            while zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                
                left += 1
            
            res = max(res, right-left+1)
        
        return res-1