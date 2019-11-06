class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def recursive(n):
            if n == 1:
                return 0
            
            if n % 2 == 0:
                return 1+recursive(n//2)
            
            else:
                
                return 1+min(recursive(n+1),recursive(n-1))
        
        return recursive(n)