class Solution:
    def findMaxValueOfEquation(self, p: List[List[int]], k: int) -> int:
        
        #max heap
        
        res = -float('inf')
        q = []
        
        for x,y in p:
            
            while q and q[0][1] < x-k:
                heapq.heappop(q)
            
            if q:
                res = max(res, -q[0][0]+y+x)
            
            heapq.heappush(q, ((x-y),x))
        
        return res
                    