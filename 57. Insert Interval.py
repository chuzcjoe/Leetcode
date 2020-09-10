class Solution:
    def insert(self, intervals: List[List[int]], newInt: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInt]
        
        cnt = 0
        idx = bisect.bisect_left(intervals, newInt)
        intervals.insert(idx, newInt)
        res = []

        
        while intervals:
            s1, e1 = heapq.heappop(intervals)
            s2, e2 = heapq.heappop(intervals)
            tmp = [[s1,e1],[s2,e2]]
            print(tmp)
            
            if s1 <= s2 and e1 >= e2:
                tmp = []
                tmp.append([s1, e1])
            elif s2 <= e1 <= e2:
                tmp = []
                tmp.append([s1,e2])
            elif s1 <= e2 <= e1:
                tmp = []
                tmp.append([s2,e1])
            
            
            if len(tmp) == 1:
                if len(intervals) == 0:
                    res.append(tmp[0])
                    break
                else:
                    heapq.heappush(intervals, tmp[0])
            elif len(tmp) == 2:
                if len(intervals) == 0:
                    res.extend(tmp)
                    break
                else:
                    res.append(tmp[0])
                    heapq.heappush(intervals, tmp[1])
        
        return res
        