class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = collections.defaultdict(list)
        courses = collections.defaultdict(list)
        
        
        for x,y in prerequisites:
            graph[x].append(y)
        
        #dfs returns a list of following courses
        def reach(s,t):
            
            if s == t:
                return True
            
            visited.add(s)
            
            for nei in graph[s]:
                if nei in visited:
                    continue
                
                elif reach(nei, t):
                    return True
            
            return False
        
        
        res = []
        
        for i,j in queries:
            visited = set()
            res.append(reach(i,j))
        
        return res
        