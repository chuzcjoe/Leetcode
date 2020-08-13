class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        """
        #1. Brute Force
        S = "0"
        
        for i in range(2,n+1):
            invert = ""
            for x in S:
                invert += str((int(x)+1) % 2)
            
            S = S + "1" + invert[::-1]
        
        return S[k-1]
        
        """
        
        #2. recursive based on symmetry
        
        if n == 1:
            return "0"
        
        length = 2**n - 1
        if k == length // 2 + 1:
            return "1"
        
        elif k <= length//2:
            return self.findKthBit(n-1,k)
        
        else:
            if self.findKthBit(n-1, length-k+1) == "0":
                return "1"
            else:
                return "0"