class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        v = ['a','e','i','o','u']
        left = 0
        res = sum(l in v for l in s[:k])
        output = res
        
        for right in range(k,len(s)):
            
            
            if s[right] in v and s[left] in v:
                res = res
            elif s[right] in v and s[left] not in v:
                res += 1
            elif s[right] not in v and s[left] in v:
                res -= 1
            elif s[right] not in v and s[left] not in v:
                res = res
            
            left += 1
            
            output = max(output, res)
            
        
        return output
        
                
                
        