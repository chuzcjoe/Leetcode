class Solution:
    def reorganizeString(self, S: str) -> str:
        
        c = collections.Counter(S)
        
        q = [(-v,k) for k,v in c.items()]
        heapq.heapify(q)
        
        #prev_v and prev_k record previous most frequent letter and its frequency
        
        prev_v, prev_k = 0, ""
        res = ""
        
        while q:
            v, k = heapq.heappop(q)
            res += k
            
            if prev_v < 0:
                heapq.heappush(q,(prev_v,prev_k))
            
            v += 1
            prev_v, prev_k = v, k
        
        if len(res) == len(S):
            return res
        else:
            return ""
            