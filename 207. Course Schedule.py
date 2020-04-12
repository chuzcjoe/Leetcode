class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        isCircle = [0 for _ in range(numCourses)]
        
        for x,y in prerequisites:
            graph[y].append(x)
        
        # 0-not visited  1-has been visited and forms no circle  -1-circle can be formed
        def dfs(cur):
            
            if isCircle[cur] == 1:
                return True
            
            elif isCircle[cur] == -1:
                return False
            
            isCircle[cur] = -1
            
            for nxt in graph[cur]:
                if not dfs(nxt):
                    return False
            isCircle[cur] = 1
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
            
        