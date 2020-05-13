class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i]:
                i += 1
                continue
            else:
                if i==n-2 or i==n-1:
                    arr[-1] = 0
                    break
                else:
                    arr[i+2:] = arr[i+1:-1]
                    arr[i+1] = 0
                    i += 2
                
            