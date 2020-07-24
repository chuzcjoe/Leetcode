class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        f = {}
        ans = []
        
        def find(x):
            f.setdefault(x,x)
            
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        graph = collections.defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
        
        for s,t in edges:
            if find(s) == find(t):
                ans.append([s,t])
            
            union(t,s)
        
        return ans[-1]