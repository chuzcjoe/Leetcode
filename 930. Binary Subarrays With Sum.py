class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        """
        # approach 1
        def help(A, S):
            left = 0
            res = 0
        
            for right in range(len(A)):
                if S < 0:
                    return 0
                
                S -= A[right]
            
                while S < 0:
                    if A[left] == 1:
                        S += 1
                    left += 1
            
                res += right - left + 1
                
            return res
        
        return help(A, S) - help(A, S-1)
        """
        
        # approach 2
        # A[i] + A[i+1] + ... + A[j] = (A[0] + A[1] + ... + A[j]) - (A[0] + A[1] + ... + A[i-1])
        #                            = sum[0:j] - sum[0:i-1] = target
        
        counter = collections.Counter({0:1})
        res = 0
        presum = 0
        for j in range(len(A)):
            presum += A[j]
            res += counter[presum - S]
            
            counter[presum] += 1
        
        return res