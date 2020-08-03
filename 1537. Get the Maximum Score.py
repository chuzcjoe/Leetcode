class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)
        dp1 = [0] * (n1+1)
        dp2 = [0] * (n2+1)
        
        i = j = 0
        
        while i < n1 or j < n2:
            if i < n1 and j < n2 and nums1[i] == nums2[j]:
                dp1[i+1] = dp2[j+1] = max(dp1[i], dp2[j]) + nums1[i]
                i += 1
                j += 1
            elif  i < n1 and (j == n2 or nums1[i] < nums2[j]):
                dp1[i+1] = dp1[i] + nums1[i]
                i += 1
            elif j < n2 and (i == n1 or nums1[i] > nums2[j]):
                dp2[j+1] = dp2[j] + nums2[j]
                j += 1
                
        return max(dp1[-1], dp2[-1]) % (10**9+7)
                
                
            
            
        
        
            