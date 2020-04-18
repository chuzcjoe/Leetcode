class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        if k > 3 * 2 ** (n-1):
            return ""
        
        letters = ['a','b','c']
        right = 0
        res = []
        
        while n > 0:
            i = 0
            while right < k:
                i += 1
                right += 2 ** (n-1)
            
            right = right - 2 ** (n-1)
            nxt = letters.pop(i-1)
            res.append(nxt)
            
            if len(letters) == 1:
                if nxt == 'a':
                    letters = ['b','c']
                elif nxt == 'b':
                    letters = ['a','c']
                elif nxt == 'c':
                    letters = ['a','b']
            
            n = n - 1
        
        return "".join(res)
        