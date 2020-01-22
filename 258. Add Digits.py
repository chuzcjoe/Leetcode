class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num = str(num)
        while len(num) != 1:
            tmp = str(sum([int(x) for x in num]))
            num = tmp
        
        return int(num)