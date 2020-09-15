class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def dist(p1, p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2) + abs(y1-y2)
        
        n = len(points)
        d = [float('inf')] * n
        cur = 0
        ans = 0
        seen = set()
        
        for i in range(n-1):
            seen.add(cur)
            for j,p in enumerate(points):
                if j in seen: continue
                d[j] = min(d[j], dist(points[cur],points[j]))
            
            min_d, nxt = min((d,j) for j,d in enumerate(d))
            d[nxt] = float('inf') #don't count distance with self
            cur = nxt
            ans += min_d
        
        return ans
                                   
                
            