class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
        lookup = {c:[s.index(c), s.rindex(c)+1] for c in set(s)}
        res = []
        
        for x in set(s):
            l = tmpl = lookup[x][0]
            r = tmpr = lookup[x][1]
            
            while True:
                for k in s[l:r]:
                    tmpl = min(tmpl, lookup[k][0])
                    tmpr = max(tmpr, lookup[k][1])
                
                if [l,r] == [tmpl, tmpr]:
                    break
                
                l = tmpl
                r = tmpr
            
            res.append([l,r])
        
        ans = []
        last = 0
        
        res = sorted(res, key=lambda x: x[1])
        
        for b,e in res:
            if b >= last:
                ans.append(s[b:e])
                last = e
        
        return ans
            
            
                
                
        
            
                
            
            
                