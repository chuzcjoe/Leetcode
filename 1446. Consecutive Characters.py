class Solution:
    def maxPower(self, s: str) -> int:
        
        res = 1
        left = 0
        
        for right in range(1, len(s)):
            
            while s[left] != s[right]:
                left += 1
            
            res = max(res, right-left+1)
        
        return res
            