class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        h = []
        counter = collections.Counter(tasks)
        for k,v in counter.items():
            heapq.heappush(h,(-v,k))
            
        interval = 0
        
        while h:
            i, temp = 0, []
            while i <= n:
                interval += 1
                if h:
                    cnt, task = heapq.heappop(h)
                    if cnt != -1:
                        temp.append((cnt+1, task))
                
                if not h and not temp:
                    break
                else:
                    i += 1
            
            for k,v in temp:
                heapq.heappush(h,(k,v))
        
        return interval
        
        
        
            
        