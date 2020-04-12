class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
            
        def slope(p1,p2):
            if p1[1] - p2[1] == 0:
                return 'H'
            elif p1[0] - p2[0] == 0:
                return 'V'
            else:

                return (p2[1] - p1[1])/(p2[0] - p1[0])
        
        
        res = 0
        
        for i in range(len(points)):
            counter = collections.Counter()
            max_points = 0
            dup = 1
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    dup += 1
                else:
                    print(slope(points[i], points[j]))
                    counter[slope(points[i], points[j])] += 1
                    max_points = max(max_points, counter[slope(points[i], points[j])])
            
            res = max(res, max_points + dup)
        
        return res
        