class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        print(dp)
        
        if dp[-1]:
            return True
        