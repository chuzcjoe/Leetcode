class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        r = len(A)
        c = len(A[0])
        dp = [[0] * c for _ in range(r)]
        
        for j in range(c):
            dp[0][j] = A[0][j]
        
        for i in range(1,r):
            for j in range(c):
                tmp = []
                if j-1>=0:
                    tmp.append(dp[i-1][j-1])
                if j+1<c:
                    tmp.append(dp[i-1][j+1])
                tmp.append(dp[i-1][j])
                
                dp[i][j] = min(tmp) + A[i][j]
        
        return min(dp[r-1][:])