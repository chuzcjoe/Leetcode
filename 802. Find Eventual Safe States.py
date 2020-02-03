class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        
        color = [0] * n
        
        #0-unvisited 1-safe 2-unsafe
        
        def dfs(graph, start, color):
            if color[start] == 1:
                return True
            
            if color[start] == 2:
                return False
            
            color[start] = 2
            
            for new in graph[start]:
                print(color,start,new)
                if not dfs(graph, new, color):
                    return False
            
            color[start] = 1
            
            return True
        
        res = []
        for node in range(len(graph)):
            if dfs(graph, node, color):
                res.append(node)
                
        return res