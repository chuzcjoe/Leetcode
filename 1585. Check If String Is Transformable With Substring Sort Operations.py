class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        
        q = [collections.deque() for _ in range(10)]
        
        for i,x in enumerate(s):
            q[int(x)].append(i)
        
        for i,a in enumerate(t):
            a = int(a)
            
            if len(q[a]) == 0:
                return False
            
            for b in range(a):
                if q[b] and q[b][0] < q[a][0]:
                    return False
            
            q[a].popleft()
        
        return True
                
        