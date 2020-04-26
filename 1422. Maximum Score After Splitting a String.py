class Solution:
    def maxScore(self, s: str) -> int:
        
        res = 0
        
        for i in range(1,len(s)):
            counter1 = collections.Counter(s[:i])
            counter2 = collections.Counter(s[i:])
            
            res = max(counter1['0'] + counter2['1'], res)
        
        return res