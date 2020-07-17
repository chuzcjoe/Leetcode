class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr = sorted(arr)
        n = len(arr)
        l = 0
        r = max(arr)
        
        diff = float('inf')
        
        def helper(value):
            tmp = None
            for i,a in enumerate(arr):
                if a > value:
                    tmp = i
                    break
            
            if tmp is None:
                tmp = n-1
                    
            return sum(arr[:tmp])+(n-tmp)*value-target
        
        while l < r-1:
            mid = (l+r) // 2
            diff = helper(mid)
            
            if diff <= 0:
                l = mid
            else:
                r = mid
        
        return l if abs(helper(l)) <= abs(helper(r)) else r