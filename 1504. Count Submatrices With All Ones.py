"""
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
"""

    
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        c = len(mat[0])
        r = len(mat)
        
        ans = 0
        
        for i in range(r-1,-1,-1):
            for j in range(c-2,-1,-1):
                if mat[i][j] == 0:
                    continue
                else:
                    mat[i][j] += mat[i][j+1]
        
        for ii in range(r):
            for jj in range(c):
                MIN = mat[ii][jj]
                ans += MIN
                
                for k in range(ii+1, r):
                    if mat[k][jj] == 0:
                        break
                        
                    MIN = min(MIN, mat[k][jj])
                    ans += MIN
        
        return ans
                
                    
                    
                
        