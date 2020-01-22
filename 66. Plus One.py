class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        s = ''
        for x in digits:
            s += str(x)
        
        s = str(int(s) + 1)
        
        return [int(x) for x in s]