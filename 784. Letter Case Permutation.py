class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def backtrack(path, option, res, seen, n):
            
            if len(path) == n and path not in seen:
                seen.add(path)
                res.append(path)
                
            
            for i in range(len(option)):
                if option[i].isdigit():
                    path += option[i]
                    backtrack(path, option[i+1:], res ,seen, n)
                else:
                    for letter in [option[i].lower(), option[i].upper()]:
                        path += letter
                        backtrack(path, option[i+1:], res, seen, n)
                        path = path[:-1]
        
        n = len(S)
        option = [x for x in S]
        res = []
        seen = set()
        
        backtrack("", option, res, seen, n)
        
        return res