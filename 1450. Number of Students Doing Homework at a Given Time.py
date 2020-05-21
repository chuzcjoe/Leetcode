class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        cnt = 0
        for s,e in zip(startTime, endTime):
            if s <= queryTime <= e:
                cnt += 1
        
        return cnt