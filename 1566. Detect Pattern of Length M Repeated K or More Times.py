class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        n = len(arr)
        if m*k > n:
            return False
        
        def check(sub):
            cnt = 1
            a = sub[:m]
            i = m
            while i < len(sub):
                if sub[i:i+m] == a:
                    cnt += 1
                else:
                    break
                
                i += m
            
            return cnt == k
        
        for right in range(m*k-1, len(arr)):
            sub = arr[right-m*k+1:right+1]
            
            if check(sub):
                return True
        
        return False
            