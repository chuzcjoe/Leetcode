class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def Palindrome(s):
            return s == s[::-1]
        
        
        def backtrack(s, path, res):
            
            if not s:
                
                res.append(path[:])
                return
                
            
            for i in range(1,len(s)+1):
                if Palindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:], path, res)
                    path.pop(-1)
        
        res = []
        backtrack(s, [], res)
        
        return res
                