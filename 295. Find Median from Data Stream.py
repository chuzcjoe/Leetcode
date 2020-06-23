class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #max heap for half small numbers
        #min heap for half large numbers
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        
        else:
            return (self.large[0]-self.small[0]) / 2
        
            
            
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()