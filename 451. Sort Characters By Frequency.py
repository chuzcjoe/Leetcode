class Solution:
    def frequencySort(self, s: str) -> str:
        
        # solution 1
        #c = collections.Counter(s)
        
        #res = sorted(c.items(), key=lambda x:x[1], reverse=True)
        
        #return "".join(r[0]*r[1] for r in res)
        
        #solution 2, max heap
        q = []
        c = collections.Counter(s)
        
        for k,v in c.items():
            heapq.heappush(q, (-v,k))
        
        res = []
        
        while q:
            tmp = heapq.heappop(q)
            res.append(tmp[1]*(-tmp[0]))
        
        return "".join(res)
            
        