class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [x for x in range(1,10)]
        
        def dfs(nums,index,res,path):
            if len(path) > k:
                return
            if len(path) == k and sum(path) == n:
                res.append(path)
            
            for i in range(index,len(nums)):
                dfs(nums,i+1,res,path+[nums[i]])
            
        dfs(nums,0,res,[])
        
        return res