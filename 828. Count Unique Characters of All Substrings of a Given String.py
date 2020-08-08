class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        letters = [chr(x) for x in range(65, 65+26)]
        ans = 0
        n = len(s)
        
        idxs = {l:[-1,-1] for l in letters}
        
        for i,a in enumerate(s):
            left, right = idxs[a]
            ans += (right-left)*(i-right)
            idxs[a] = [right, i]
            
        for idx in idxs:
            left, right = idxs[idx]
            ans += (n-right)*(right-left)
        
        return ans % (10**9+7)
            
            
        
        