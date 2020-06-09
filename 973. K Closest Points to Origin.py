class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def distance(x,y):
            return x**2+y**2
        
        q = []
        
        for x,y in points:
            if len(q) == K:
                heapq.heappushpop(q, [-distance(x,y),x,y])
            else:
                heapq.heappush(q, [-distance(x,y),x,y])
        
        return [[x,y] for _,x,y in q]