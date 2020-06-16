class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        #binary search
        left = 1
        right = max(bloomDay)
        
        while left < right:
            mid = (left+right) // 2
            
            flow = bouq = 0
            
            for f in bloomDay:
                flow = 0 if f > mid else flow + 1
                
                if flow >= k:
                    bouq += 1
                    flow = 0
                    
                    if bouq == m:
                        break
                
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        
        return left
        