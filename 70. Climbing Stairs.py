class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return None
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
            
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n-1]
        