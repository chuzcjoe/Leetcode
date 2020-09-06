class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        #always remove the peak elements
        n = len(arr)
        res = n+1
        left, right = 0, n-1
        
        for i in range(0, n-1):
            if arr[i] <= arr[i+1]:
                left += 1
            else:
                break
        
        for j in range(n-1, 0, -1):
            if arr[j] >= arr[j-1]:
                right -= 1
            else:
                break
        
        if left == n-1:
            return 0
        
        res = min(res, n-1-left, right)
        
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j-i-1)
                i += 1
            else:
                j += 1
        
        return res
        
        
                
            