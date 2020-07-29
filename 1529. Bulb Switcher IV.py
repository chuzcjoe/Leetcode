class Solution:
    def minFlips(self, target: str) -> int:
        
        ans = 0
        light = False #the current bulb status
        
        for b in target:
            if b == '1' and not light:
                ans += 1
                light = True
            
            elif b == '0' and light:
                ans += 1
                light = False
        
        return ans
            
            
            