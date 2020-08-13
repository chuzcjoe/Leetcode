class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        prefix = collections.defaultdict(int)
        prefix[0] = -1
        s = 0
        ans = 0
        last = -1
        
        for i,a in enumerate(nums):
            s += a
            
            if s - target in prefix and prefix[s-target] >= last:
                ans += 1
                last = i
            
            prefix[s] = i
        
        return ans
            