class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        

        c1 = collections.Counter([x**2 for x in nums1])
        c2 = collections.Counter([y**2 for y in nums2])
        ans = 0
        print(c1,c2)
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                p = nums2[i]*nums2[j]
                ans += c1[p]
        
        
        for ii in range(len(nums1)):
            for jj in range(ii+1, len(nums1)):
                p = nums1[ii]*nums1[jj]
                ans += c2[p]
        
        return ans
        
        