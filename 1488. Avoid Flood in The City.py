class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        dic = collections.defaultdict(list)
        to_empty = []
        res = [-1] * len(rains)
        
        for i,r in enumerate(rains):
            dic[r].append(i)
        
        for j in range(len(rains)):
            lake = rains[j]
            
            if lake:
                if dic[lake] and dic[lake][0] < j:
                    return []
                
                if dic[lake] and len(dic[lake]) > 1:
                    #the first lake we see that we need to empty
                    heapq.heappush(to_empty, dic[lake][1])
            
            else:
                if to_empty:
                    res[j] = rains[heapq.heappop(to_empty)]
                    dic[res[j]].pop(0)
                else:
                    res[j] = 1
        
        return res
                
                    
        
        
        