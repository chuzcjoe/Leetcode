class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        
        def is_tri(L):
            return L[1] + L[2] > L[0]
        
        A.sort()
        A = A[::-1]
        
        for i in range(len(A)-2):
            if is_tri([A[i],A[i+1],A[i+2]]):
                return A[i] + A[i+1] + A[i+2]
                
        
        return 0