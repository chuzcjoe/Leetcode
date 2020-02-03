class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        """
        #1
        count = collections.Counter({0:1})
        
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y+x] += count[y]
                step[y-x] += count[y]
            
            count = step
        
        return count[S]
        """
        
        #2
        summary = sum([abs(x) for x in nums])
        n = len(nums)
        
        #dp[i][j] means the number of ways for first i-th numbers to reach j
        dp = [[-1]*(2*summary+1) for _ in range(n+1)]
        
        for i in range(2*summary+1):
            dp[0][i] = 0
        dp[0][summary] = 1
        
        if summary < S:
            return 0
        
        def DP(k,S):
            if S < 0 or S >= 2 * summary + 1:
                return 0
            
            if dp[k][S] == -1:
                dp[k][S] = DP(k-1,S-nums[k-1]) + DP(k-1,S+nums[k-1])
            return dp[k][S]
        
        DP(n, summary+S)
        return dp[n][summary+S]
            
        