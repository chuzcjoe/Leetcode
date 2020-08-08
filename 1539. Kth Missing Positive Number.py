class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        ALL = set(list(range(1,1001)))
        
        missing = sorted(ALL - set(arr))
        n = len(missing)
        
        arr = set(arr)
        
        if k > n:
            return 1000 + k - n
                
        
        else:
            return missing[k-1]
        