class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
            
        r = len(matrix)
        c = len(matrix[0])
        
        dp = [[0]*c for _ in range(r)]
        

        for i,row in enumerate(matrix):
            for j, e in enumerate(row):
                dp[i][j] = int(e)
                if int(e) and i and j:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
        
  
        print(dp)
        return max(map(max,dp)) ** 2