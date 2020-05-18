class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        res = 0
        while len(arr) > 1:
            
            minIdx = arr.index(min(arr))
            
            if 0 < minIdx < len(arr)-1:
                res += min(arr[minIdx-1], arr[minIdx+1]) * arr[minIdx]
            else:
                res += (arr[minIdx+1] if minIdx == 0 else arr[minIdx-1]) * arr[minIdx]
            
            arr.pop(minIdx)
        
        return res