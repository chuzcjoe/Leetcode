class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        diff = A[-1] - A[0]
        flg = diff >= 0
        
        for i in range(len(A)-1):
            if A[i+1] == A[i]:
                continue
                
            if ((A[i+1]-A[i]) >= 0) != flg:
                return False
        
        return True
                
        