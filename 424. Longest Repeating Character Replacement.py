class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        left = res = 0
        n = len(s)
        counter = collections.Counter()
        
        for right in range(n):
            counter[s[right]] += 1
            
            while sum(sorted(list(counter.values()))[:-1]) > k:
                counter[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
            
        return res