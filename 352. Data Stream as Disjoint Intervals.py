class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.seen = set()
        
    """
    def addNum(self, val: int) -> None:
        if not self.res:
            self.res.append([val,val])
        else:
            idx = bisect.bisect_left(self.res, [val])
            if idx == len(self.res) and self.res[idx-1][1] >= val:
                return
            
            if idx == 0 and val+1 < self.res[0][0]:
                self.res.insert(0, [val,val])
            elif idx == 0 and val+1 == self.res[0][0]:
                MAX = self.res[0][1]
                self.res[0] = [val, MAX]
            elif idx == len(self.res) and val-1 > self.res[-1][1]:
                self.res.append([val,val])
            elif idx == len(self.res) and val-1 == self.res[-1][1]:
                MIN = self.res[-1][0]
                self.res[-1] = [MIN, val]
            elif self.res[idx-1][1] < val-1 and self.res[idx][0] > val + 1:
                self.res.insert(idx, [val,val])
            elif self.res[idx-1][1] + 1 == val and self.res[idx][0] - 1 == val:
                MIN = self.res[idx-1][0]
                MAX = self.res[idx][1]
                self.res.pop(idx-1)
                self.res.pop(idx-1)
                self.res.insert(idx-1, [MIN,MAX])
            elif self.res[idx-1][1] + 1 == val:
                MIN = self.res[idx-1][0]
                self.res[idx-1] = [MIN, val]
            elif self.res[idx][0]-1 == val:
                MAX = self.res[idx][1]
                self.res[idx] = [val, MAX]
    """
    
    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.res, [val,val])
                

    def getIntervals(self) -> List[List[int]]:
        tmp = []
        
        while self.res:
            cur = heapq.heappop(self.res)
            
            if tmp and cur[0] <= tmp[-1][1]+1:
                tmp[-1][1] = max(cur[1], tmp[-1][1])
            else:
                tmp.append(cur)
            
        self.res = tmp
        return self.res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()