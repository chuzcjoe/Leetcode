class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = 0
        prefix = []
        for i,a in enumerate(nums):
            total += a
            prefix.append(total)
        
        for i,a in enumerate(nums):
            left = prefix[i] - a
            right = prefix[len(nums)-1] - prefix[i]
            
            if left == right:
                return i
        
        return -1