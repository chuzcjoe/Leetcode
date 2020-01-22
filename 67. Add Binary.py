class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        result = [0] * (max(len(a),len(b))+1)
        
        n = max(len(a),len(b))
        #keep same length
        s1 = '0' * (n - len(a))
        s2 = '0' * (n-len(b))
        a = s1 + a
        b = s2 + b
        incre = 0
        
        i = -1
        while i >= -n:
            
            if int(a[i]) + int(b[i]) + incre >= 2:
                result[i] = (int(a[i]) + int(b[i]) + incre) % 2
                incre = 1
            else:
                result[i] = int(a[i]) + int(b[i]) + incre
                incre = 0
                
            i -= 1
        
        if incre:
            result[0] = 1
        else:
            result = result[1:]
        
        return ''.join([str(x) for x in result])
            
        