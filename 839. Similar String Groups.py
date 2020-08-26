class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        
        if not A:
            return 0
        
        A = set(A)
        
        f = {}
        def find(x):
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        seen = set()
        
        for a in A:
            find(a)
            seen.add(a)
            old = list(a)
            for i in range(len(a)-1):
                for j in range(i+1,len(a)):
                    if old[i] == old[j]:
                        continue
                    tmp = old.copy()
                    tmp[i],tmp[j] = tmp[j],tmp[i]
                    tmp = "".join(tmp)
                    if tmp in seen:
                        union(a,tmp)
        
        ans = set(map(find, f))
        
        return len(ans)
            
            
                
                    
                    
            
        
                
                