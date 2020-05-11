class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        left = 0
        res = 0
        minq = []
        maxq = []
        
        for right,x in enumerate(nums):
            heapq.heappush(minq, [x,right])
            heapq.heappush(maxq, [-x,right])
            
            while -maxq[0][0]-minq[0][0] > limit:
                left = min(maxq[0][1], minq[0][1]) + 1
                
                while maxq[0][1] < left: heapq.heappop(maxq)
                while minq[0][1] < left: heapq.heappop(minq)
                
            res = max(res, right-left+1)
        
        return res
                
                
        