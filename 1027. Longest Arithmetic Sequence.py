class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        dp = collections.defaultdict(int)
        
        for i,a in enumerate(A[1:], start=1):
            for j,b in enumerate(A[:i]):
                d = a-b
                if (j,d) in dp:
                    dp[(i,d)] = dp[(j,d)] + 1
                else:
                    dp[(i,d)] = 2
        
        return max(dp.values())
        