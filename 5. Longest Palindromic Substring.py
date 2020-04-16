class Solution:
    def longestPalindrome(self, s):
        
        n = len(s)
        res = ""
        
        def helper(s, l, r):
            while l >=0 and r < n and s[l]==s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]
        
        for i in range(n):
            
            # odd palindrome
            tmp = helper(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            
            # even palindrome
            tmp = helper(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        
        return res
            
        
        
            
        