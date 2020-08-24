class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        f = {}
        n = len(arr)
        ans = -1
        ranks = [0] * (n+1)
        
        if m == n:
            return m
        
        def find(x):
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            px,py = find(x), find(y)
            
            if ranks[px] > ranks[py]:
                ranks[px] += ranks[py]
                f[py] = px
            else:
                ranks[py] += ranks[px]
                f[px] = py

            
        for i,a in enumerate(arr):
            ranks[a] = 1
            
            for j in [a-1,a+1]:
                if 1<= j <= n:
                    if ranks[find(j)] == m:
                        ans = i
                    if ranks[j]:
                        union(a,j)
        
        return ans