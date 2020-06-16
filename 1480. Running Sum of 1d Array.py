class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = []
        pre = 0
        
        for n in nums:
            pre += n
            res.append(pre)
        
        return res