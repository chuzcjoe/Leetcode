class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        
        def distance(x,y):
            return sum(sqrt((x-x_)**2+(y-y_)**2) for x_,y_ in positions)
        
        xc, yc = sum(x for x, _ in positions)/len(positions), sum(y for _, y in positions)/len(positions)
        
        d = distance(xc, yc)
        
        step = 10
        eps = 0.000001
        
        while step > eps:
            flg = False
            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                x2 = xc + step*dx
                y2 = yc + step*dy
                t = distance(x2,y2)
                
                if t < d:
                    xc,yc = x2, y2
                    d = t
                    flg = True
            
            if not flg:
                step = step / 2
        
        return d
        