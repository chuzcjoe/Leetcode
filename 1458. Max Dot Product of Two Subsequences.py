class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0] * len(nums1) for _ in range(len(nums2))]
        
        res = -1001
        for i in range(len(nums2)):
            res = max(nums1[0]*nums2[i], res)
            dp[i][0] = res
        
        res = -1001
        for j in range(len(nums1)):
            res = max(nums1[j]*nums2[0], res)
            dp[0][j] = res
        
        for i in range(1,len(nums2)):
            for j in range(1,len(nums1)):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1], max(dp[i-1][j-1], 0)+nums2[i]*nums1[j])
        
        
        return dp[len(nums2)-1][len(nums1)-1]
        