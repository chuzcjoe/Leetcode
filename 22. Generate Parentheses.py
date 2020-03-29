class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def ismatch(s):
            tmp = []
            for i in range(len(s)):
                if not tmp:
                    tmp.append(s[i])
                    continue
                
                
                if s[i] == ')' and tmp[-1] == '(':
                        tmp.pop(-1)
                else:
                        tmp.append(s[i])
            
            return not tmp
                    
        
        def backtrack(path, n, res):
            
            if len(path) > 2*n:
                return
                
            if len(path) == 2*n and ismatch(path):
                res.append(path)
                return
            
            for s in ["(", ")"]:
                path += s
                backtrack(path, n ,res)
                path = path[:-1]
        
        res = []
        backtrack("(", n ,res)
        
        return res