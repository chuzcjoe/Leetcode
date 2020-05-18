class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        def helper(s,l,r, visited):
            
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (l,r) not in visited:
                    visited.add((l,r))
                    
                l -= 1
                r += 1
        
        visited = set()
        
        for i in range(len(s)):
            
            #odd palindrom
            helper(s,i,i,visited)
            
            #even plindrom
            helper(s,i,i+1,visited)
        
        return len(visited)