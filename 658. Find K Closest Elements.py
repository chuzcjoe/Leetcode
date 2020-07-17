class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        q = []
        
        for a in arr:
            heapq.heappush(q, (abs(x-a), a))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(q)[1])
        
        return sorted(ans)