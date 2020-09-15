class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = []
        col_sum = []
        
        r = len(mat)
        c = len(mat[0])
        ans = 0
        
        for i in range(r):
            s = 0
            for j in range(c):
                s += mat[i][j]
            row_sum.append(s)
        
        for m in range(c):
            s = 0
            for n in range(r):
                s += mat[n][m]
            col_sum.append(s)
        
        for x in range(r):
            for y in range(c):
                if mat[x][y] == 1 and row_sum[x] == 1 and col_sum[y] == 1:
                    ans += 1
        
        return ans
                