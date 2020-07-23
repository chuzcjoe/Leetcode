class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        
        ans = float('inf')
        s1 = set()
        m = 0
        
        for a in arr:
            s2 = set([a])
            
            for e in s1:
                s2.add(e&a)
            
            for e in s2:
                ans = min(ans, abs(e-target))
            
            s1 = s2
            
        return ans
                
                
            