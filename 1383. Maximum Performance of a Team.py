class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        h = []
        res = 0
        sUM = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            
            sUM += s
            
            if len(h) > k:
                sUM -= heappop(h)
            
            res = max(res, sUM * e)
        
        return res % (10**9 + 7)