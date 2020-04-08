class Solution:
    def numSteps(self, s: str) -> int:
       
        num = 0
        
        num = sum([int(n)*2**i for i,n in enumerate(s[::-1])])
        
        
        step = 0
        
        while num != 1:
            
            if num & 1:
                num += 1
            else:
                num = num // 2
            
            step += 1
        
        return step