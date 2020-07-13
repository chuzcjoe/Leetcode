class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        #dp[i]: the results of having i stones
        #if we can have dp[i-K^2] = False, then dp[i] must be True cuz we can move K^2 stones and win the game
        
        dp = [False] * (n+1)
        
        for i in range(n+1):
            dp[i] = not all(dp[i-k**2] for k in range(1, int(i**0.5)+1) if i-k**2>=0)
        
        return dp[-1]