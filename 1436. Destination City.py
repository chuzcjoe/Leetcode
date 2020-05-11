class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        g = collections.defaultdict(int)
        cities = set()
        for x,y in paths:
            g[x] += 1
            cities.add(x)
            cities.add(y)
        
        for c in cities:
            if g[c] == 0:
                return c
            
            
            
        