class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        res = None
        for i in range(n):
            if i == 0:
                res = start + 2*i
            else:
                res ^= start + 2*i
        
        return res
        
        