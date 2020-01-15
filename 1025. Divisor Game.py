class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        
        
        dp = []
        dp.append(1) 
        
        for i in range(2,N+1):
            flag = False
            for j in range(1,i):
                if i % j == 0 and i - j in dp:
                    flag = True
                    break
            if not flag:
                dp.append(i)
                
        if N in dp:
            return False
        else:
            return True
        
        
        