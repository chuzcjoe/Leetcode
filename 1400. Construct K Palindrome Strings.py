class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False
        
        if len(s) == k:
            return True
        
        odd_nums = [i for i in collections.Counter(s).values() if i % 2 == 1]
        
        return len(odd_nums) <= k <= len(s)
        
        
        