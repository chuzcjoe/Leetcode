class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        
        #dp[k][i] 0-i numbers are devided into k group and the maximum sum
        
        dp = [[0]*len(A) for _ in range(K+1)]
        presum = [0]*len(A)
        
        #compute the prefix sum to get the avg value in O(1), and initialize k=1
        for i,a in enumerate(A):
            if i == 0:
                presum[i] = a
            else:
                presum[i] = presum[i-1]+a
            
            dp[1][i] = presum[i] / (i+1)
        
        #transition: dp[k][i] = max(dp[k-1][j]+avg(A[j+1],A[j+2],...,A[i]))
        
        for k in range(2,K+1):
            for i in range(k-1,len(A)):
                for j in range(i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + (presum[i]-presum[j])/(i-j))
        
        return dp[K][len(A)-1]
        
        