class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        
        
        while l < r:
            m = (l+r) // 2
            
            cnt = 0
            res = 0
            for w in weights:
                if res + w > m:
                    cnt += 1
                    res = w
                elif res + w == m:
                    cnt += 1
                    res = 0
                else:
                    res += w
            
            cnt += 1
            
            
            if cnt <= D:
                r = m
            else:
                l = m + 1
        
        return l
                
                
            
            