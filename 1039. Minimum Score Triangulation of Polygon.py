class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        
        #dp[i][j] for i to j, the min triangle sum we can get
        n = len(A)
        dp = [[0]*n for i in range(n)]
        for l in range(2, n):
            for left in range(0, n - l):
                right = left + l
                dp[left][right] = float("inf")
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + A[left]*A[right]*A[k])
        return dp[0][-1]
        