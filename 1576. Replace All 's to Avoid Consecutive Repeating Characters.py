class Solution:
    def modifyString(self, s: str) -> str:
        
        choices = set(chr(i) for i in range(97,97+26))
        
        s = list(s)
        left, right = None, None
        
        for j,a in enumerate(s):
            if a == "?":
                left = s[j-1] if j > 0 else None
                right = s[j+1] if j < len(s)-1 else None
                c = copy.deepcopy(choices)
                c -= {left, right}
                s[j] = c.pop()
        
        return "".join(s)