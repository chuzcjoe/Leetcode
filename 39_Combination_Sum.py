class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        res = []
        
        def dfs(candidates,res,path):
            if sum(path) == target:
                path = sorted(path)
                if path not in res:
                    res.append(path)
                return
            
            if sum(path) > target:
                return 
            
            for i in range(0,len(candidates)):
                #if sum(path) > target:
                #    break
                dfs(candidates,res,path+[candidates[i]])
        
        dfs(candidates,res,[])
        
        return res