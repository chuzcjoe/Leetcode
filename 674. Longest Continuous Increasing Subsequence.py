class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        
        start = 0
        res = 0
        
        for i in range(len(nums)):
            if i == len(nums)-1:
                res = max(res, i-start+1)
                break
                
            if nums[i] >= nums[i+1]:
                res = max(res, i-start+1)
                start = i+1
        
        return res