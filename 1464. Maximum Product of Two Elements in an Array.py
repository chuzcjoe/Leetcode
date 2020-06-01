class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] -= 1
        
        nums = sorted(nums)
        
        return max(nums[0]*nums[1], nums[-2]*nums[-1])
        