class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)
        s2 = sorted(s2)
        flg = s1 >= s2
        
        print(flg)
        
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
                
            elif (s1[i] > s2[i]) != flg:
                return False
        
        return True