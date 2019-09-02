class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums = sorted(nums)
        
        def dfs(nums,index,res,path):
            if path in res:
                pass
            else:
                res.append(path)
            
            for i in range(index,len(nums)):
                dfs(nums,i+1,res,path+[nums[i]])
        
        dfs(nums,0,res,[])
        return res