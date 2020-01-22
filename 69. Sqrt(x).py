class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        lo = 0
        hi = x
        
        while lo <= hi:
            mid = (lo+hi) // 2
            if mid ** 2 > x:
                hi = mid - 1
            elif mid ** 2 < x:
                lo = mid + 1
            else:
                return mid
        
        return lo - 1
            
        