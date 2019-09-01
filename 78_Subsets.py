class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        
        if not nums:
            return output
            
        for elem in nums:
            output.extend([x + [elem] for x in output])
            
        return output