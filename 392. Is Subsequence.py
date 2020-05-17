class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = list(s)
        
        for x in t:
            if not s:
                return True
            if x == s[0]:
                s.pop(0)
        
        return False if s else True
                