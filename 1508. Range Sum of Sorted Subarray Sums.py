class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        """
        1. brute force
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for j in range(i, len(nums)):
                prefix += nums[j]
                ans.append(prefix)
        
        ans = sorted(ans)
        return sum(ans[left-1:right])
        """
        
        q = []
        ans = 0
        for i,a in enumerate(nums):
            q.append([a,i])
        
        heapq.heapify(q)
        
        for j in range(1, right+1):
            x, i = heapq.heappop(q)
            if j >= left:
                ans += x
            
            if i+1 < len(nums):
                heapq.heappush(q, [x+nums[i+1], i+1])
        
        return ans % (10**9+7)
        
        
        
        