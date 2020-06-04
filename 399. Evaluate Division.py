class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = collections.defaultdict(list)
        
        def build_graph(eq, val):
            
            for e, v in zip(eq, val):
                f,t = e[0], e[1]
                graph[f].append((t,v))
                graph[t].append((f,1/v))
        
        def dfs(s, e, product, seen):
            print(s,e,product)
            if s not in graph or e not in graph:
                return -1.0
            
            if s == e:
                return product
            
            seen.add(s)
            tmp = 0
            for nei,val in graph[s]:
                if nei not in seen:
                    tmp = dfs(nei, e, val*product, seen)
                    if tmp != -1:
                        return tmp
            
            return -1.0
            
        build_graph(equations, values)
        
        res = []
        for q1,q2 in queries:
            seen = set()
            res.append(dfs(q1,q2,1,seen))
        
        return res
        
        
        