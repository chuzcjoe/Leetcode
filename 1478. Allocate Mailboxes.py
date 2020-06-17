class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        
        n = len(houses)
        houses = sorted(houses)
        
        # cost[i][j]: min total distance for house group [i:j]
        cost = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i,n):
                median = houses[(i+j)//2]
                for t in range(i,j+1):
                    cost[i][j] += abs(median-houses[t])
        
        # dp[i][j]: min total distance to houses[:i] use j+1 mailboxes
        dp = [[10**6]*k for _ in range(n)]
        for i in range(n):
            dp[i][0] = cost[0][i]
        
        for kk in range(1, k):
            for ii in range(n):
                for jj in range(ii):
                    dp[ii][kk] = min(dp[ii][kk], dp[jj][kk-1]+cost[jj+1][ii])
        
        return dp[-1][-1]
        
                