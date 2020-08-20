class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        half = (m+n) // 2
        ALL = nums1 + nums2
        
        #larger part
        minq = []
        
        #smaller part
        maxq = []
        
        for a in ALL:
            heapq.heappush(maxq, -a)
            
            if len(maxq) > half:
                v = heapq.heappop(maxq)
                heapq.heappush(minq, -v)
        
        return minq[0] if (m+n)%2 else (minq[0]-maxq[0]) / 2
        
        
        
        
        