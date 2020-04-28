class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #similar to two sum, base case + 2 sum
        
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)-2):
            # since nums are sorted in increasing order
            if nums[i] > 0:
                break
            #nums[i] has been used as base
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L = i+1
            R = len(nums)-1
            
            while L < R:
                
                s = nums[i]+nums[L]+nums[R]
                
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    res.append([nums[i],nums[L],nums[R]])
                    while L < R and nums[L]==nums[L+1]:
                        L += 1
                    while L < R and nums[R]==nums[R-1]:
                        R -= 1
                    
                    L += 1
                    R -= 1
            
        return res
        