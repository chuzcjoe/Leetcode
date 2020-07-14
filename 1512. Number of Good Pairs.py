class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        cnt = collections.Counter(nums)
        ans = 0
        
        for k,v in cnt.items():
            ans += v*(v-1)//2
        
        return ans