class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        total = 2 ** k
        res = set()
        
        for i in range(0, len(s)-k+1):
            res.add(s[i:i+k])
        
        
        if len(res) == total:
            return True
        else:
            return False