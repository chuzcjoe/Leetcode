class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        k = len(nums)
        save = set()
        nums = sorted(nums)
        
        def dfs(nums,index,res,path):
            
            if len(path) == k:
                if tuple(path) in save:
                    return
                else:
                    res.append(path)
                    save.add(tuple(path))
            
            for i in range(0,len(nums)):
                dfs(nums[:i]+nums[i+1:],0,res,path+[nums[i]])
                
        dfs(nums,0,res,[])
        
        return res