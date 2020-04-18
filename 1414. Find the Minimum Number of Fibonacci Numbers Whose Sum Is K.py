class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        if k < 2:
            return k
        
        a = b = 1
        
        while b <= k:
            # a,b are FibonacciNumbers that a and b are adjancent and a < b
            a, b = b, a+b
        
        return self.findMinFibonacciNumbers(k-a) + 1
        