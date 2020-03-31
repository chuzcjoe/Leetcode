class Solution:
    def longestPrefix(self, s: str) -> str:
        
        MAX = 0
        res = ""
        for i in range(0,len(s)):
            if s[:i] == s[len(s)-i:]:
                if i > MAX:
                    res = s[:i]
                    MAX = i
        
        return res
        
        