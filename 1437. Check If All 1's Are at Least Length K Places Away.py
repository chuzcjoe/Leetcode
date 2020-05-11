class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        left = -1
        right = -1
        
        for i, x in enumerate(nums):
            if x:
                left = right
                right = i
                if left!=-1 and right - left - 1 < k:
                    return False
        
        return True
            