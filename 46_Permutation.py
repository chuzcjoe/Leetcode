class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        k = len(nums)
        def dfs(nums,index,res,path):
            if len(path) == k:
                res.append(path)
                return
            
            
            for i in range(0,len(nums)):
                    dfs(nums[:i]+nums[i+1:],0,res,path+[nums[i]])
        
        dfs(nums,0,res,[])
        
        return res
        