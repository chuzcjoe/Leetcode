class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        
        pos = sorted(pos)
        left = 0
        right = pos[-1]-pos[0]
        
        def count(d):
            cnt = 1
            cur = pos[0]
            for i in range(1,len(pos)):
                if pos[i] - cur >= d:
                    cnt += 1
                    cur = pos[i]
                    
            return cnt
                
        
        while left < right:
            mid = right - (right-left) // 2
            
            c = count(mid)
            
            if c >= m:
                left = mid
            else:
                right = mid - 1
        
        return left
        
            
            
        
        