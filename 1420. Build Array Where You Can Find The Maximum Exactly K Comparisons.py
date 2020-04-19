class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        #dp[i][j][k], when length equals to 1 and cost equals to j, the largest value is k
        if m < k:
            return 0
        N = n
        M = m
        K = k
        dp = [[[0 for _ in range(m+1)] for _ in range(k+1)] for _ in range(n+1)]
        
        # when len==1 and cost ==1
        for i in range(1,m+1):
            dp[1][1][i] = 1
        
        #for i, j, k in itertools.product(range(1, n + 1), range(1, k + 1), range(m + 1)):
        for i in range(1,N+1):
            for j in range(1,K+1):
                for k in range(M+1):
                    # case 1:  from dp[i-1][j][k] to dp[i][j][k], cost remains the same
                    dp[i][j][k] += dp[i-1][j][k] * k
                    
                    # case 2: from dp[i-1][j-1][kk] to dp[i][j][k], where kk < k
                    dp[i][j][k] += sum(dp[i-1][j-1][1:k])
                    
        return sum(dp[N][K][1:M+1]) % (10**9 + 7)
        