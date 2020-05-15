class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left = seats.index(1)
        res = 0
        res = max(res, left)
        
        for right in range(left+1, len(seats)):
            if right == len(seats)-1 and seats[right]==0:
                res = max(res, right-left)
                break
                
            if seats[right]:
                res = max(res, (right-left)//2)
                left = right
        
        return res
                