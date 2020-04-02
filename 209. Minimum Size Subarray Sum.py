class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        left = 0
        n = len(nums)
        res = n + 1
        
        for right in range(n):
            s -= nums[right]
                
            
            while s <= 0:
                res = min(res, right - left + 1)
                s += nums[left]
                left += 1
                
        if res == n+1:
            return 0
        else:
            return res
                
            