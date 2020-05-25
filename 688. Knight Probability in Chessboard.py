class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        #dp[k][i][j] means when i moves k steps, the probability that i land on cell (i,j)
        
        dp = [[[0] * N for _ in range(N)] for _ in range(K+1)]
        moves = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
        
        dp[0][r][c] = 1
        
        for k in range(0,K):
            for i in range(N):
                for j in range(N):
                    if dp[k][i][j] == 0:
                        continue
                    for dx,dy in moves:
                        if 0 <= i+dx < N and 0 <= j+dy < N:
                            dp[k+1][i+dx][j+dy] += 0.125 * dp[k][i][j]
        
        return sum(dp[K][rr][cc] for rr in range(N) for cc in range(N))
                        