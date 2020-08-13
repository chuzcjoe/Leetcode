class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.extend([0,n])
        cuts = sorted(cuts)
        
        dp = [[0]*len(cuts) for _ in range(len(cuts))]
        
        def helper(i,j):
            if dp[i][j] or i+1 == j:
                return dp[i][j]
            
            cost = float('inf')
            for k in range(i+1,j):
                cost = min(cost, cuts[j]-cuts[i]+helper(i,k)+helper(k,j))
            
            dp[i][j] = cost
            
            return cost
        
        return helper(0, len(cuts)-1)