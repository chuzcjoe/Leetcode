class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)
        if len(arr) == 1 or len(arr) == 2:
            return True
        
        diff = arr[1] - arr[0]
        
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return False
        
        return True
            