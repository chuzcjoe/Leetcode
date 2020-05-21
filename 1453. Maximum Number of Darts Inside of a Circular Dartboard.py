class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        
        # a sub function that calculates the center of the circle
        def compute_center(p1, p2, r):
            (x1, y1), (x2, y2) = p1, p2

            # delta x, delta y between points
            dx, dy = x1-x2, y1-y2

            # dist between points
            q = math.sqrt(dx**2+dy**2)

            # if two points are too far away, there is no such circle
            if q > 2*r:
                return []

            # find the halfway point
            x3=(x1+x2)/2
            y3=(y1+y2)/2

            # distance along the mirror line
            d = math.sqrt(r**2-(q/2)**2)

            # One circle
            c1 = [x3 - d*dy/q, y3 + d*dx/q]

            # The other circle
            c2 = [x3+d*dy/q, y3-d*dx/q]
            
            return [c1, c2]
        
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                
                centers = compute_center(points[i], points[j], r)
                
                for c in centers:
                    cnt = 0
                    for p in points:
                        if (c[0]-p[0])**2+(c[1]-p[1])**2 <= r**2+10**(-6):
                            cnt += 1
                    
                    res = max(res, cnt)
        
        return res if res else 1
                    
            