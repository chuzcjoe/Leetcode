class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        fre = collections.defaultdict(int)
        for b in barcodes:
            fre[b] += 1
        
        q = []
        for k,v in fre.items():
            heapq.heappush(q, (-v,k))
        
        prev_v = 0
        prev_k = None
        
        res = []
        while q:
            a, b = heapq.heappop(q)
            a += 1
            res.append(b)
            
            if prev_v < 0:
                heapq.heappush(q, (prev_v, prev_k))
            
            prev_v = a
            prev_k = b
        
        return res
            