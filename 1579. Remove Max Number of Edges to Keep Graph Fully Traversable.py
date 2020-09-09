class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        f = {}
        e1 = e2 = ans = 0
        
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return 0
            
            f[px] = py
            return 1
        
        for t,a,b in edges:
            if t == 3:
                if union(a,b):
                    e1 += 1
                    e2 += 1
                else:
                    ans += 1
        
        f_copy = copy.deepcopy(f)
        
        for t,a,b in edges:
            if t == 1:
                if union(a,b):
                    e1 += 1
                else:
                    ans += 1
        
        f = f_copy
        for t,a,b in edges:
            if t == 2:
                if union(a,b):
                    e2 += 1
                else:
                    ans += 1
        
        return ans if e1 == e2 == n-1 else -1