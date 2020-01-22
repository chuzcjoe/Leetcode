class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]] = i
        