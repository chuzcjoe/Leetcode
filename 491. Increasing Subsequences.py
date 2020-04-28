class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path, nums, start, res):
            
            if len(path) >= 2 and path not in res:
                res.append(path[:])
            
            for i in range(start, len(nums)):
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    backtrack(path[:], nums, i+1, res)
                    path.pop()
        
        if not nums:
            return []
        
        res = []
        backtrack([], nums, 0, res)
        
        return res
        