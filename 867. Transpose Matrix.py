class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        r = len(A)
        c = len(A[0])
        
        new = [[0]*r for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                new[j][i] = A[i][j]
        
        return new