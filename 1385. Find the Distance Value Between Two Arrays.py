class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        res = 0
        for a1 in arr1:
            for a2 in arr2:
                if -d <= a1 - a2 <= d:
                    res += 1
                    break
        
        return len(arr1) - res
        
        
        
        