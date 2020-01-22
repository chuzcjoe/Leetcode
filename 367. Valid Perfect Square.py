class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        lo = 0
        hi = num
        
        while lo <= hi:
            mid = (lo+hi) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False