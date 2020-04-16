class Solution:
    def isValid(self, s: str) -> bool:
        
        queue = collections.deque()
        parens = [['(',')'], ['{','}'], ['[',']']]
        right_parens = [')',']','}']
        
        for x in s:
            if not queue:
                queue.append(x)
            
            elif x in right_parens:
                if [queue[-1], x] in parens:
                    queue.pop()
                else:
                    break
            else:
                queue.append(x)
        
        if not queue:
            return True
        else:
            return False
                
        