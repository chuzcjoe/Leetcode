class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = sorted(satisfaction)
        
        res = 0
        MAX = -10**32
        
        for i in range(len(s)):
            time = 1
            for j in range(i,len(s)):
                res += s[j] * time
                time += 1
            MAX = max(res, MAX)
            res = 0
        
        MAX = 0 if MAX < 0 else MAX
        
        return MAX