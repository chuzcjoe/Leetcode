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
    
        """
        class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        """
        output = [[]]
        
        if not nums:
            return output
            
        for elem in nums:
            print(elem)
            output.extend([x + [elem] for x in output])
            print(output)
        return output
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res
    
        def dfs(self, nums, index, res, path):
            print(res)
            res.append(path)
            for i in xrange(index, len(nums)):
                self.dfs(nums, i + 1, res, path + [nums[i]])
            
        """
