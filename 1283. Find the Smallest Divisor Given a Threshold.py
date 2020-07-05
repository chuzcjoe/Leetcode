class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        
        while l < r:
            m = (l+r) // 2
            
            tmp = 0
            for n in nums:
                if n % m == 0:
                    tmp += n // m
                else:
                    tmp += n // m + 1
            
            if tmp > threshold:
                l = m+1
            else:
                r = m
        
        return l
            
            