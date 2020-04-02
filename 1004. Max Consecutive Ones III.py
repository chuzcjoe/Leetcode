class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        left = 0
        res = 0
        zeros = 0
        
        n = len(A)
        
        
        for right in range(n):
            if A[right] == 0:
                zeros += 1
            
            while zeros > K:
                if A[left] == 0:
                    left += 1
                    zeros -= 1
                else:
                    left += 1
            
            res = max(res, right - left + 1)
            
        
        return res
        
            
        