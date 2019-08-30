class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        res, num, sign = 0,0,1
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                #print(num)
            elif c in '+-':
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                num = 0
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                preSign = stack.pop()
                preRes = stack.pop()
                res = preRes + preSign * res
                num = 0
                sign = 1
        return res + sign * num
        