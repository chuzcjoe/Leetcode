class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        ans = ""
        
        s = str(n)[::-1]
        
        for i,a in enumerate(s):
            ans += a
            
            if i == len(s)-1:
                break
                
            if (i+1) % 3 == 0:
                ans += "."
        
        return ans[::0-1]
                
            