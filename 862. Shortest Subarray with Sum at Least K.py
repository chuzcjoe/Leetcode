class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        d = collections.deque([[0,0]])
        res = len(A) + 1
        cur = 0
        
        for i,x in enumerate(A):
            
            cur += x
            
            while d and cur-d[0][1] >= K:
                res = min(res, i+1-d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
                
            d.append([i+1, cur])
        
        return res if res < len(A)+1 else -1
                
            
        