class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        """
        Solution 1: DP
        pairs = sorted(pairs)
        dp = [1] * len(pairs)
        
        for i in range(1,len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)

        return dp[-1]
        """
        
        """
        Solution 2: Greedy
        """
        
        cur, res = -float('inf'), 0
        
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur = p[1]
                res += 1
        
        return res
            
