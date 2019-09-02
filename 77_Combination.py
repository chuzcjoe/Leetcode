class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        nums = [x for x in range(1,n+1)]
        
        res = []
        
        def dfs(nums, index, res, path):
            if len(path) == k:
                res.append(path)
                return
            #else:
            #    pass
            
            
            for i in range(index,len(nums)):
                dfs(nums,i+1,res,path+[nums[i]])
                
        
        dfs(nums,0,res,[])
        
        return res