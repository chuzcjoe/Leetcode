class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        f = {}
        
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        for eq in equations:
            if eq[1:3] == '==':
                union(eq[0], eq[-1])
        
        for noneq in equations:
            if noneq[1:3] == '!=' and find(noneq[0]) == find(noneq[-1]):
                return False
        

        return True