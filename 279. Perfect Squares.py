class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = []
        i = 1
        while 1:
            if i**2 > n:
                break
            else:
                nums.append(i**2)
                i += 1
        print(nums)
        dp = [0] * (n+1)
        dp[1] = 1
        for j in range(2,n+1):
            idxs = [j-num for num in nums if j >= num]
            dp[j] = min([dp[idx]+1 for idx in idxs])
            
        print(dp)
        return dp[n]
        
