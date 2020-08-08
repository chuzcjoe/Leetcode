class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = collections.defaultdict(int)
        for a,b in zip(s,t):
            
            diff = (ord(b)-ord(a)) % 26
            if diff == 0:
                continue
            
            if diff > k:
                return False
            
            d[diff] += 1
            if (d[diff]-1)*26+diff > k:
                return False
        
        
        return True