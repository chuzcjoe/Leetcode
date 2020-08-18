class MajorityChecker:

    def __init__(self, arr: List[int]):
        
        self.idx = collections.defaultdict(list)
        for i,a in enumerate(arr):
            self.idx[a].append(i)
        
        tmp = sorted(self.idx.items(), key=lambda x: len(x[1]), reverse=True)
        
        self.order = [x for x,_ in tmp]

    def query(self, left: int, right: int, threshold: int) -> int:
        
        for k in self.order:
            if len(self.idx[k]) < threshold:
                return -1
            l = bisect.bisect_left(self.idx[k], left)
            r = bisect.bisect_right(self.idx[k], right)
            if r-l >= threshold:
                return k
        
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)