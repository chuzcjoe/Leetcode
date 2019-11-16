class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        m = len(triangle)
        
        if m == 1:
            return triangle[0][0]
        
        dp = [[0]*i for i in range(1,m+1)]
        dp[0][0] = triangle[0][0]
        
        
        for i in range(1,m):
            for j in range(0,i+1):
                l = j-1 if j >= 1 else None
                r = j if j < len(triangle[i-1]) else None
                poses = [p for p in [l,r] if p != None]
                #print(poses)
            
                #val = [triangle[i][p] for p in poses]
            
                
                dp[i][j] = triangle[i][j] + min([dp[i-1][p] for p in poses])
                
            
            
                
        print(dp)
        return min(dp[m-1])
            
                
        
