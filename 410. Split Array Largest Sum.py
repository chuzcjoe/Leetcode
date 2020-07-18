class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        lo = max(nums)
        hi = sum(nums)
        
        def possible(x):
            cur = 0
            split = 1
            for a in nums:
                if cur+a <= x:
                    cur += a
                else:
                    split += 1
                    cur = a
            
            return split <= m
                    
        ans = 0
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if possible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans
        