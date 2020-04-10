class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        n1 = len(s1)
        n2 = len(s2)
        
        def backtrack(path, option):
            
            nonlocal res
            if len(path) == n1:
                res.append(path)
                return
            
            for i in range(len(option)):
                path.append(option[i])
                backtrack(path[:], option[:i]+option[i+1:])
                path = path[:-1]
        
        res = []
        backtrack([], s1)
        res = ["".join(x) for x in res]

        for i in range(n2-n1+1):
            if s2[i:i+n1] in res:
                return True
            
        
        return False
        """
        n1 = len(s1)
        n2 = len(s2)
        counter = collections.Counter(s1)
        
        for i in range(n2-n1+1):
            if collections.Counter(s2[i:i+n1]) == counter:
                return True
        return False
        
        
        