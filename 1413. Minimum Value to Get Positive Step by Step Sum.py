class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        res = []
        s = 0
        for x in nums:
            s += x
            res.append(1-s)
            
        if max(res) <= 0:
            return 1
        else:
            return max(res)