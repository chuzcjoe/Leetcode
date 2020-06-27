class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        
        child = collections.defaultdict(set)
        parent = collections.defaultdict(list)
        ends = []
        visited = set()
        semester = 0
        indi = set(range(1,n+1))
        
        for x,y in dependencies:
            child[x].add(y)
            parent[y].append(x)
            indi = indi - {x,y}
        
        #find no incoming nodes
        for node in range(1, n+1):
            if node not in child and node not in indi:
                ends.append([node,semester])
        
        while len(visited) != n:
            print(ends)
            for i in range(k):
                if not ends:
                    if indi:
                        visited.add(indi.pop())
                    continue
                if ends and ends[0][1] == semester + 1:
                    if indi:
                        visited.add(indi.pop())
                    continue
                    
                cur, sem = ends.pop(0)
                visited.add(cur)
                ps = parent[cur]
                if not ps:
                    continue
                else:
                    for p in ps:
                        child[p].remove(cur)
                        if not child[p]:
                            ends.append([p, sem+1])
            
            semester += 1
        
        return semester
                
                
        