class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        nums = sorted(nums, reverse=True)
        
        s = 0
        res = sum(nums) //2
        select = []
        
        for x in nums:
            s += x
            if s <= res:
                select.append(x)
            else:
                select.append(x)
                break
        
        return select