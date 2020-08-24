class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = 0
        
        while sum(nums) != 0:
            tmp = nums.copy()
            ones_tmp = nums.copy()
            cnt = 0
            ones_cnt = 0
            flag = False
            for i,a in enumerate(nums):
                if a == 1:
                    ones_cnt += 1
                    ones_tmp[i] = 0
                    flag = True
                
                tmp[i] = nums[i] // 2
                cnt += nums[i] % 2
            
            if flag:
                ans += ones_cnt
                nums = ones_tmp[:]
            else:
                ans += cnt + 1
                nums = tmp[:]
        
        return ans
                
                    