class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = []
        
        for i,x in enumerate(s):
            
            if ans:
                pre = ans[-1]
                if ord(pre) != ord(x) and (pre.lower() == x or x.lower() == pre):
                    ans.pop(-1)
                
                else:
                    ans.append(x)
            
            else:
                ans.append(x)
        
        return "".join(ans)
            
             