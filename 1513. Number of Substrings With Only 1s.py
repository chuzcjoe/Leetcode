class Solution:
    def numSub(self, s: str) -> int:
        
        left = 0
        ans = 0
        right = 0
        
        while right < len(s):
            if s[right] == '1':
                ans += right - left + 1
                right += 1
            else:
                while right < len(s) and s[right] == '0':
                    right += 1
                
                if right == len(s):
                    break
                
                left = right
                
        return ans % (10**9+7)
        