class Solution:
    def longestAwesome(self, s: str) -> int:
        
        ans = 0
        state = 0
        #for tracking the first position of each state
        dp = [-1] + [len(s)] * 1024
        
        for i,a in enumerate(s):
            v = int(a)
            state ^= 1 << v
            
            for j in range(10):
                ans = max(ans, i-dp[state^(1<<j)])
                
            ans = max(ans, i-dp[state])
            dp[state] = min(dp[state], i)
        
        return ans