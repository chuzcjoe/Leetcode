class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv',
               '9':'wxyz'}
        
        res = []
        k = len(digits)
        
        if not digits:
            return []
        
        def dfs(digits,nums,i,res,path):
            #print(path)
            if len(path) == k:
                res.append(path)
                return
            if i == k:
                return
            for w in nums[digits[i]]:
                dfs(digits,nums,i+1,res,path+w)
                
            
        dfs(digits,nums,0,res,'')
        
        return res
            
            