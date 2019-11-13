class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        def recursive(N):
            if N == 1:
                return 1
        
            if N == 0:
                return 0
        
            
            return recursive(N-1)+recursive(N-2)
        
        return recursive(N)
        