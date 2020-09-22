class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        mod = 10**9 + 7
        n = len(nums)
        res = 0
        
        t = [0] * (n+1)
        
        for a,b in requests:
            t[a] += 1
            t[b+1] -= 1
        
        for i in range(1,len(t)):
            t[i] += t[i-1]
        
        t.pop(-1)
        t.sort()
        
        nums.sort()
        
        for x,y in zip(t,nums):
            res += x*y
        
        return res % mod
            
                