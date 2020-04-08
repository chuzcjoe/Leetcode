class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        counter = collections.Counter()
        n = len(s)
        left = 0
        res = 0
        
        for right in range(n):
            counter[s[right]] += 1
            
            while any(x > 1 for x in counter.values()):
                counter[s[left]] -= 1
                left += 1
                
            res = max(res, right-left+1)
        
        return res