class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        
        
  
        """
        1. DFS (LTE)
        
        g1 = collections.defaultdict(int)
        g2 = collections.defaultdict(list)
        
        for s, d, p in flights:
            g1[(s,d)] = p
            g2[s].append(d)
        min_cost = float('inf')
        
        def dfs(node, dst, cost, steps):
            nonlocal min_cost
            
            if steps > K+1:
                return
            
            if node == dst:
                min_cost = min(min_cost, cost)
                return
            
            
            for nei in g2[node]:
                dfs(nei, dst, cost+g1[(node, nei)], steps+1)
        
        dfs(src, dst, 0, 0)
        
        return -1 if min_cost==float('inf') else min_cost
        """
    
        #2. heap
        
        dic = collections.defaultdict(dict)
        
        for s,d,p in flights:
            dic[s][d] = p
        
        q = [(0,src,K+1)]
        
        while q:
            p, cur, steps = heapq.heappop(q)
            
            if cur == dst:
                return p
            
            if steps > 0:
                for nei in dic[cur]:
                    heapq.heappush(q, (p+dic[cur][nei], nei, steps-1))
        
        return -1
                
            
            
        
    
    
        
        
        
        
        
            
            