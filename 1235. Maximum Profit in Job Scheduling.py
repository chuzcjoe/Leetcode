class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        com = []
        
        for s,e,p in zip(startTime, endTime, profit):
            com.append([s,e,p])
        
        com = sorted(com, key=lambda x:x[1])
        
        dp = [[0,0]]
        
        for s,e,p in com:
            i = bisect.bisect(dp, [s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1]+p])
        
        return dp[-1][1]
        
        