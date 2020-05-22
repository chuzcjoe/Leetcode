class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        #dp[i][j] minimum clips to form i-j
        dp = [[float('inf')]*(T+1) for _ in range(T+1)]
        
        for x,y in clips:
            for j in range(x,y+1):
                if x>T or j>T:
                    break
                    
                dp[x][j] = 1
                
        
        for i in range(T+1):
            if dp[0][i] == 1:
                continue
            
            for k in range(1,i):
                dp[0][i] = min(dp[0][i], dp[0][k]+dp[k][i])
        
        return -1 if dp[0][T]==float('inf') else dp[0][T]
        