class Solution:
    def maxDiff(self, num: int) -> int:
        
        def replace1(num):
            s = str(num)
            if s[0] != '9':
                s = s.replace(s[0],'9')
                return int(s)
            else:
                i = 0
                while i < len(s) and s[i] == '9':
                    i += 1
                
                if i == len(s):
                    return int(s)
                else:
                    return int(s.replace(s[i],'9'))
        
        def replace2(num):
            s = str(num)
            if s[0] != '1':
                s = s.replace(s[0],'1')
                return int(s)
            else:
                i = 0
                while i < len(s) and s[i] in ['0','1']:
                    i += 1
                
                if i == len(s):
                    return int(s)
                else:
                    return int(s.replace(s[i],'0'))
        
        d1 = replace1(num)
        d2 = replace2(num)
        print(d1,d2)
        
        return abs(d1-d2)