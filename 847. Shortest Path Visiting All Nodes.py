class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        G = collections.defaultdict(list)
        
        for node in range(len(graph)):
            for nei in graph[node]:
                G[node].append(nei)
        
        target = (1 << len(graph)) - 1
        start = [[1<<j, j] for j in range(len(graph))]
        seen = {(1<<i, i) for i in range(len(graph))}
        q = collections.deque(start)
        step = 0
        
        
        while q:
            size = len(q)
            for _ in range(size):
                state, node = q.popleft()
                if state == target:
                    return step
                
                for nei in G[node]:
                    new_state = state | (1 << nei)
                    if (new_state, nei) not in seen:
                        seen.add((new_state, nei))
                        q.append([new_state, nei])
            
            step += 1
                
        
        