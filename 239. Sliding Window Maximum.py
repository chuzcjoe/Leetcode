class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        d = collections.deque()
        
        for i,n in enumerate(nums):
            #make sure the most right index in d points to the largest value
            #in nums
            while d and nums[d[-1]] <= n:
                d.pop()
                
            d.append(i)
            
            if d[0] == i-k:
                d.popleft()
            
            if i+1 >= k:
                res.append(nums[d[0]])
        
        return res
            
                