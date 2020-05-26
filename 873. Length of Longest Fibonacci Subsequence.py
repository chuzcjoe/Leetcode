class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        m = collections.defaultdict(int)
        for i,a in enumerate(A):
            m[a] = i
        
        #dp[i][j] max len of seq ending with A[i],A[j]
        #dp[k][i]+1 = dp[i][j]
        
        ans = 0
        
        for i in range(1, n):
            for j in range(i+1,n):
                if A[j] - A[i] >= A[i]:
                    break
                
                if A[j]-A[i] in m:
                    idx = m[A[j]-A[i]]
                
                    dp[i][j] = dp[idx][i] + 1
                    ans = max(ans, dp[i][j])
        
        return 0 if ans == 2 else ans