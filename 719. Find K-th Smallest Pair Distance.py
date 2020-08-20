class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        
        
        def count(d):
            cnt = 0
            
            for i in range(1, len(nums)):
                a = nums[i]
                j = bisect.bisect_left(nums[:i+1], a-d)
                cnt += i - j
            
            return cnt
        
        l = 0
        r = nums[-1]-nums[0]
        
        while l < r:
            
            mid = l + (r-l)//2
            
            c = count(mid)
            
            print(mid, c)
            
            if c < k:
                l = mid + 1
            else:
                r = mid
        
        return l
            
            
        
        
                
            