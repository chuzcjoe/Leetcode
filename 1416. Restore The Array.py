class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        n = len(s)
        LEN = len(str(k))
        
        dp = [0] * n
        if 1 <= int(s[0]) <= k:
            dp[0] = 1
            
        
        for i in range(1,n):
            for j in range(LEN):
                if i-j > 0:
                    if s[i-j] != '0' and int(s[i-j:i+1]) <= k:
                        dp[i] += dp[i-j-1]
                elif i-j == 0:
                    if 1 <= int(s[i-j:i+1]) <= k:
                        dp[i] += 1
        
        return dp[-1] % (10**9 + 7)