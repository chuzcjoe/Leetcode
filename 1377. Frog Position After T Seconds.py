class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        
        nei = collections.defaultdict(set)
        for x,y in edges:
            nei[x].add(y)
            nei[y].add(x)
            
        # node 1 is 100% at time 0
        queue = collections.deque([(1,1,0)])
        
        visited = set()
        
        while queue:
            
            node, prob, time = queue.popleft()
            visited.add(node)
            
            if time > t:
                continue
                
            if time == t and node == target:
                return prob
            
            neighbors = nei[node] - visited
            
            for n in neighbors or [node]:
                queue.append((n, prob/(len(neighbors) or 1) or 0, time+1))
        
        return 0