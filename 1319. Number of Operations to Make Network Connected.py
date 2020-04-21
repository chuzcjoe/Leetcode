class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        #DFS solition
        
        cables = len(connections)
        graph = collections.defaultdict(list)
        
        
        if cables < n - 1:
            return -1
        
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)

        seen = [0] * n
        
        def dfs(i):
            if seen[i]:
                return 0
            seen[i] = 1
            
            for j in graph[i]:
                dfs(j)
            
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
    
        
    
        
       
        
        
            