class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        
        while l < r:
            m = (l+r) // 2
            
            tmp = 0
            for p in piles:
                if p % m == 0:
                    tmp += p // m
                else:
                    tmp += p // m +1
            
            if tmp > H:
                l = m+1
            else:
                r = m
        
        return l