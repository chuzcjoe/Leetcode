class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        check = list(A[0])
        
        for word in A[1:]:
            new_check = []
            
            for s in word:
                if s in check:
                    new_check.append(s)
                    #this step is the key
                    check.remove(s)
                    
            check = new_check
        
        return check
            
                
                
        
        