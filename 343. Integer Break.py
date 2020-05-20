class Solution:
    def integerBreak(self, n: int) -> int:
        
        #when n=4, res = 2*2
        #when n =5, res = 2*3
        #when n=6, res = 3*3
        
        #pattern:
        #if n is even, if we choose two nums, res = (N//2)*(N//2)
        #if n is odd, res = (N//2-1)*(N//2+1)
        
        # if n > 4 we can always breaks it down into two numbers, such as:
        # 9 = 5*4, however 5->2*3, 4->2*2
        #note: we want as many 3 as possible since 6=2+2+2=3+3
        
        if n==2:
            return 1
        if n==3:
            return 2
        
        product = 1
        while n > 4:
            product *= 3
            n -=3
        
        return product*n