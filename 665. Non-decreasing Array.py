class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        res = 0
        arr1 = nums[:]
        arr2 = nums[:]
        
        
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                arr1[i] = nums[i+1]
                arr2[i+1] = nums[i]
                break
        
        flg1 = flg2 = True
        
        for i in range(len(nums)-1):
            if arr1[i] > arr1[i+1]:
                flg1 = False
            
            if arr2[i] > arr2[i+1]:
                flg2 = False
        
        return flg1 or flg2
            
        