class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        x = str(x)[::-1]
        idx = 0
        
        for i,num in enumerate(x):
            if num != '0':
                idx = i
                break
            
        
        return int(x[idx:]) * sign if abs(int(x[idx:])) < 2 ** 31 else 0
        