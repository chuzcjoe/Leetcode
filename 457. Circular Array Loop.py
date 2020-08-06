class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        for i,a in enumerate(nums):
            flg = str(i)
            tmp = i
            
            while type(nums[tmp]) != str and a*nums[tmp] > 0 and nums[tmp] % n != 0:
                jump = nums[tmp]
                nums[tmp] = flg
                tmp = (tmp+jump) % n
            
            if nums[tmp] == flg:
                return True
        
        
        return False
