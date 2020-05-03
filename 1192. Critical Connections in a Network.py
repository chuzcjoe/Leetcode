class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = collections.defaultdict(list)
        
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            
        """
        BFS: TLE
        
        res = []
        for i in range(n):
            graph[connections[i][0]].remove(connections[i][1])
            graph[connections[i][1]].remove(connections[i][0])
            level = [0]
            visited = set()
            #BFS
            while level:
                node = level.pop(0)
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        level.append(nei)
            
            if len(visited) != n:
                res.append(connections[i])
                
            
            
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])
        
        return res
        """
        
        """
        Tarjan algorithm for finding critical edges.
        """
        def dfs(id, prev, node):
            visited.add(node)
            low[node] = id
            
            for nei in graph[node]:
                
                if nei == prev:
                    continue
                if nei not in visited:
                    dfs(id+1, node, nei)
                
                low[node] = min(low[node], low[nei])
                
                if id < low[nei]:
                    res.append([node, nei])
        
        visited = set()
        low = {}
        res = []
        dfs(0,-1,0)
        
        return res
        