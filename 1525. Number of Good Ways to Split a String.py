class Solution:
    def numSplits(self, s: str) -> int:
        
        ans = 0
        
        c1 = collections.defaultdict(int)
        c2 = collections.Counter(s)
        
        for i in range(0, len(s)-1):
            c1[s[i]] += 1
            c2[s[i]] -= 1
            if c2[s[i]] == 0:
                del c2[s[i]]
            
            if len(c1.keys()) == len(c2.keys()):
                ans += 1
        
        return ans
            