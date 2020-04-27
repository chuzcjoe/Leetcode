class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = collections.defaultdict(list)
        T = [0] + [float('inf')] * N
        q = collections.deque([[0,K]])
        
        for source, target, time in times:
            graph[source].append([target, time])
        
        while q:
            time, node = q.popleft()
            
            if time < T[node]:
                T[node] = time
                
                for nxt,t in graph[node]:
                    q.append([time+t, nxt])
        
        return -1 if max(T) == float('inf') else max(T)
        
        
            
        
        