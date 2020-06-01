class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        
        graph = collections.defaultdict(list)
        c = set()
        
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            c.add((x,y))
            
        
        def dfs(node, prev):
            nonlocal res
            
            if (prev, node) in c:
                res += 1
            
            for nei in graph[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        
        res = 0
        dfs(0,-1)
        return ress