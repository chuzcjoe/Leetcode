class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        
        def help(A, K):
            left = 0
            res = 0
            counter = collections.Counter()
            for right in range(len(A)):
                if counter[A[right]] == 0:
                    K -= 1
                
                counter[A[right]] += 1
                
                while K < 0:
                    counter[A[left]] -= 1
                    if counter[A[left]] == 0:
                        K += 1
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return help(A, K) - help(A, K-1)
                    
                    
                