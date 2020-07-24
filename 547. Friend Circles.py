class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        f = {}
        
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j]:
                    union(i,j)
        
        
        return len(set(map(find, f)))