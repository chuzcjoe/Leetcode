class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) < 3:
            return False
        
        peak = False
        idx = 0
        
        for i,a in enumerate(A[:-1]):
            #we only need the first peak and its index
            if A[i] >= A[i+1] and not peak:
                peak = True
                idx = i
            
            if A[i] <= A[i+1] and peak:
                return False
        
        return False if not peak or idx==0 or idx==len(A)-1 else True