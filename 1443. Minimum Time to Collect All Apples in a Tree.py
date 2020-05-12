class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = collections.defaultdict(list)
        
        for f,t in edges:
            graph[f].append(t)
        
        print(graph)
        
        def dfs(node, prev):
            nonlocal steps
            
            for nei in graph[node] or [node]:
                if nei == node:
                    break
                elif nei != prev:
                    dfs(nei, node)
            
            if hasApple[node] and node!=0:
                steps += 2
                
                if prev:
                    hasApple[prev] = True
            
        steps = 0
        
        dfs(0, None)
        
        return steps
        