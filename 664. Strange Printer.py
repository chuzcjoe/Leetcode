class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        
        def dp(i,j):
            if i > j:
                return 0
            if (i,j) not in memo:
                ans = 1 + dp(i+1,j)
                for k in range(i+1,j+1):
                    if s[i] == s[k]:
                        ans = min(ans, dp(i,k-1)+dp(k+1,j))
            
                memo[(i,j)] = ans
            
            return memo[(i,j)]
        
        return dp(0, len(s)-1)