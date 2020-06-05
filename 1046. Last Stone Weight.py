class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxq = []
        
        for s in stones:
            heapq.heappush(maxq, -s)
        
        while len(maxq) > 1:
            q1 = heapq.heappop(maxq)
            q2 = heapq.heappop(maxq)
            
            if -q1-(-q2) == 0:
                continue
            else:
                heapq.heappush(maxq, q1-q2)
        
        return 0 if len(maxq) == 0 else -heapq.heappop(maxq)