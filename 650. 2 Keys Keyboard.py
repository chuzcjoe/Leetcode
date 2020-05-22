class Solution:
    def minSteps(self, n: int) -> int:
        
        def factor(x):
            res = {1}
            for i in range(2, x//2):
                if x%i == 0:
                    res.add(i)
                    res.add(x//i)
            return res
        
        #dp[i] min step to get i
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 0
        
        #if i is even: dp[i] = min(dp[i//2]+2, dp[1]+(i-1))
        #if i is odd, dp[i] = min(dp[i//2], dp[1]+(i-1))
        
        for i in range(2, n+1):
            #i is odd
            if i&1:
                factors = factor(i)
                print(factors)
                for f in factors:
                    dp[i] = min(dp[i], dp[f]+(i//f))
            #i is even
            else:
                dp[i] = min(dp[i//2]+2, dp[1]+i)
        
        print(dp)
        
        return dp[n]
        