class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        
        prefix = 0
        res = []
        for i in A:
            prefix = (prefix << 1) + i
            if prefix % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res