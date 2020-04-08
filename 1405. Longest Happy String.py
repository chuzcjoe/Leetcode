class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        res = ""
        exclude = ['aaa','bbb','ccc']
        dic = {'a':a,'b':b,'c':c}
        
        def backtrack(path, option):
            nonlocal res
            
            if any([x in path for x in exclude]):
                return
            
            if len(path) > len(res):
                res = path[:]
            
            for s in option:
                if path.count(s) >= dic[s]:
                    continue
                path += s
                backtrack(path, option)
                path = path[:-1]
        
        backtrack("", 'abc')
        
        if not res:
            return ""
        
        else:
            return res
        """
        res = ""
        while a+b+c > 0:
            if a == max(a,b,c):
                if res[-2:] != 'aa':
                    res += 'a'
                    a -= 1
                elif max(b,c) > 0:
                    if b > c:
                        res += 'b'
                        b -= 1
                    else:
                        res += 'c'
                        c -= 1
                else:
                    break
                    
            elif b == max(a,b,c):
                if res[-2:] != 'bb':
                    res += 'b'
                    b -= 1
                elif max(a,c) > 0:
                    if a > c:
                        res += 'a'
                        a -= 1
                    else:
                        res += 'c'
                        c -= 1
                else:
                    break
                    
            
            elif c == max(a,b,c):
                if res[-2:] != 'cc':
                    res += 'c'
                    c -= 1
                elif max(a,b) > 0:
                    if a > b:
                        res += 'a'
                        a -= 1
                    else:
                        res += 'b'
                        b -= 1
                else:
                    break
        return res