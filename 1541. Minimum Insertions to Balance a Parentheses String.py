class Solution:
    def minInsertions(self, s: str) -> int:
        
        cnt = 0
        s = s.replace("))","#")
        stack = []
        
        for a in s:
            
            if a == "(":
                stack.append(a)
            
            else:
                if stack:
                    stack.pop()
                    
                    if a == ")":
                        cnt += 1
                else:
                    if a == ")":
                        cnt += 1
                    
                    cnt += 1
        
        return cnt + len(stack) * 2
            
                
        
                
            