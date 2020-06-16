class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], t: int) -> int:
        
        c = collections.Counter(arr)
        
        q = []
        
        for k,v in c.items():
            heapq.heappush(q, (v,k))
        
        while t:
            fre, num = heapq.heappop(q)
            fre -= 1
            t -= 1
            
            if fre == 0:
                continue
            else:
                heapq.heappush(q, (fre, num))
        
        return len(set([n for _,n in q]))