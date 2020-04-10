class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        def diff(c1, c2):
            return abs(ord(c1)-ord(c2))
        
        
        left = res = 0
        
        for right in range(len(s)):
            maxCost -= diff(s[right], t[right])
            
            while maxCost < 0:
                maxCost += diff(s[left], t[left])
                left += 1
            
            res = max(res, right-left+1)
            
        return res
        