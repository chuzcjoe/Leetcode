class Solution:
    def balancedString(self, s: str) -> int:
        
        counter = collections.Counter(s)
        
        left = 0
        limit = len(s) // 4
        n = len(s)
        
        res = n
        
        for right in range(len(s)):
            
            counter[s[right]] -= 1
            
            while all([counter[x] <= limit for x in 'QWER']):
                if left > right:
                    return 0
                res = min(res, right - left + 1)
                counter[s[left]] += 1
                left += 1
                
        
        return res
            
            
        