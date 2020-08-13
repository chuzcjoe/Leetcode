class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        S = "0"
        
        for i in range(2,n+1):
            invert = ""
            for x in S:
                invert += str((int(x)+1) % 2)
            
            S = S + "1" + invert[::-1]
        
        return S[k-1]