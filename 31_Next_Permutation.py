class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        index = 0
        
        for i in range(len(nums)-1,0,-1):
            #print(i)
            if nums[i] > nums[i-1]:
                index = i
                break
        
        if index == 0 :
            #print('error')
            nums[:] = nums[::-1]
        else:
            right = nums[index:]
            left = nums[:index]
        
            pivot = nums[index-1]
            # find the next greater number in right
            right_copy = right
            right_copy = sorted(right_copy)
            val = [x for x in right_copy if x > pivot][0]
        
            idx = right.index(val) + len(left)
            nums[index-1],nums[idx] = nums[idx], nums[index-1]
        
            new_right = nums[index:]
            new_right = sorted(new_right)
            nums[index:] = new_right       