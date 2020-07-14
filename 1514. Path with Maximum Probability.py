class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        probs = collections.defaultdict(int)
        
        for i, (x,y) in enumerate(edges):
            graph[x].append(y)
            graph[y].append(x)
            probs[(x,y)] = succProb[i]
            probs[(y,x)] = succProb[i]
        
        queue = collections.deque([(1,start)])
        visited = collections.defaultdict(int)
        ans = -float('inf')
        
        
        while queue:
            
            prob, pos = queue.popleft()
            
            if pos == end:
                ans = max(ans, visited[pos])
            
            #visited[pos] = prob
            
            for nei in graph[pos]:
                if nei not in visited:
                    visited[nei] = prob * probs[(pos, nei)]
                    queue.append((visited[nei], nei))
                else:
                    if prob * probs[(pos, nei)] > visited[nei]:
                        visited[nei] = prob * probs[(pos, nei)]
                        queue.append((visited[nei], nei))
        
        return ans if ans != -float('inf') else 0