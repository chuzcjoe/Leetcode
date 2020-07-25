class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        f = {}
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            
            return f[x]
        
        def union(x,y):
            f[find(x)] = find(y)
        
        
        for i in range(0, len(row), 2):
            union(i, i+1)
        
        for j in range(0, len(row), 2):
            union(row[j], row[j+1])
        
        return len(row)//2 - len(set(map(find, f)))