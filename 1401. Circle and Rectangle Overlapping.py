class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # let's make rec center as origin and convert circle center
        
        x_center = abs(x_center - (x1+x2)/2)
        y_center = abs(y_center - (y1+y2)/2)
        
        # half size
        half_rx = abs(x1-x2) / 2
        half_ry = abs(y1-y2) / 2
        
        # two center distance
        
        d = (x_center**2 + y_center**2) ** 1/2
        
        x_p = abs(x1-x2)/2 if x_center >= half_rx else x_center
        y_p = abs(y1-y2)/2 if y_center >= half_ry else y_center
        
        return (x_p-x_center)**2+(y_p-y_center)**2 <= radius ** 2