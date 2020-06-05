class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        
        res = []
        flg = False
        
        for i,s in enumerate(string):
            if s == ' ' and res == []:
                continue
            
            elif (s in ['+','-'] and res == []) or (s.isdigit() and res == []):
                res.append(s)
                flg = True
            
            elif not s.isdigit() and res == []:
                break
            
            elif flg and s.isdigit():
                res.append(s)
            
            elif flg and not s.isdigit():
                break
            
        print(res)
        
        if res == [] or (len(res) == 1 and res[0] in ['+','-']):
            return 0
        
        output = int("".join(res))
        if output < -2**31:
            return -2**31
        elif output > 2**31-1:
            return 2**31-1
        else:
            return output
            
            
        