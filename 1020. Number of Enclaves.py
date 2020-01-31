class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        r = len(A)
        c = len(A[0])
        
        def dfs(x,y):
            if 0 <= x < r and 0 <= y < c and A[x][y]:
                A[x][y] = 0
                
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
            
            else:
                return
        
        for i in range(0,r):
            for j in range(0,c):
                if i == 0 or j == 0 or i == r-1 or j == c-1:
                    dfs(i,j)
        
        cnt = 0
        for i in range(r):
            for j in range(c):
                if A[i][j]:
                    cnt += 1
        
        return cnt