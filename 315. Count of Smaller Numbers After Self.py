class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sorted_arr = []
        res = []
        
        for num in nums[::-1]:
            idx = bisect.bisect_left(sorted_arr, num)
            res.append(idx)
            sorted_arr.insert(idx, num)
        
        return res[::-1]