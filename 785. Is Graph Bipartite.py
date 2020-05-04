class Solution:
    def isBipartite(seslf, graph: List[List[int]]) -> bool:
        
        g = collections.defaultdict(list)
        
        
        for i,nodes in enumerate(graph):
            for n in nodes:
                g[i].append(n)
        
        """
        DFS:
        
        def dfs(i, flg):
            nonlocal visited, res
            if not res:
                return

            if flg:
                visited[i] = 1
                for nei in g[i]:
                    if visited[nei] == 1:
                        res = False
                        return
                    if visited[nei] == 0:
                        dfs(nei, False)
            else:
                visited[i] = 2
                for nei in g[i]:
                    if visited[nei] == 2:
                        res = False
                        return
                    if visited[nei] == 0:
                        dfs(nei, True)
        
        visited = [0] * len(graph)
        for i in range(len(graph)):
            res = True
            if visited[i]:
                continue
            dfs(i, True)
            if not res:
                return False

        
        return True
        """
        
        """
        BFS
        """
        color = {}
        for i in range(len(graph)):
            if i not in color and g[i]:
                color[i] = 1
                q = collections.deque([i])
            
                while q:
                
                    cur = q.popleft()
                
                    for nei in g[cur]:
                        if nei not in color:
                            color[nei] = -color[cur]
                            q.append(nei)
                        elif color[nei] == color[cur]:
                            return False
                
        return True
            
            
                    
            
            
            
            
            
        