class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        def ways(arr):
            if len(arr) <= 2:
                return 1
            l = [x for x in arr if x < arr[0]]
            r = [x for x in arr if x > arr[0]]
            
            return math.comb(len(l)+len(r), len(l)) * ways(l) * ways(r)
        
        return (ways(nums) - 1) % (10**9+7)
        
        