class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates = sorted(candidates)
        
        res = []
        
        def dfs(candidates,index,res,path):
            
            if sum(path) > target:
                return
            if sum(path) == target and path not in res:
                res.append(path)
            
            for i in range(index,len(candidates)):
                dfs(candidates,i+1,res,path+[candidates[i]])
        
        
        dfs(candidates,0,res,[])
        
        return res