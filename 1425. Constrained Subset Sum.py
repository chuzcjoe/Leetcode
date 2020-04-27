class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        #dp transition:
        #dp[i] = max(dp[i-k], dp[i-k+1], ..., dp[i-1], 0) + nums[i]
        #dp[i] is the max sum of nums[:i]
        
        # `q` stores dp[i - k], dp[i-k+1], .., dp[i - 1] whose values are larger than 0 in a decreasing order
        q = collections.deque()
        dp = [0] * len(nums)

        
        for i in range(len(nums)):
            if q:
                dp[i] = nums[i] + q[0]
            else:
                dp[i] = nums[i] + 0
            
            while q and dp[i] >= q[-1]:
                q.pop()
            
            if dp[i] > 0:
                q.append(dp[i])
            
            if i >= k and q and q[0] == dp[i-k]:
                q.popleft()
            
        return max(dp)
            
        
        