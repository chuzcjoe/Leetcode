class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        
        """
        cnt = 0
        res = s1
        
        def change(s,i,new):
            return s[:i] + new + s[i+1:]
        
        while res <= s2:
            
            if evil not in res and s1 <= res <= s2:
                cnt += 1
                
            flag = False
            if ord(res[-1]) + 1 > 122:
                flag = True
                i = n-2
                res = change(res,n-1,'a')
                while i >= 0:
                    if flag:
                        if ord(res[i]) + 1 > 122:
                            res = change(res,i,'a')
                            flag = True
                        else:
                            res = change(res,i,chr(ord(res[i])+1))
                            
                    i -= 1
            else:
                res = change(res,n-1,chr(ord(res[-1])+1))
        """
        
        option1 = []
            
            
                    
                           
        return cnt % (10**9 + 7)
                           
            
                
        