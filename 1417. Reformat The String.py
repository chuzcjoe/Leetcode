class Solution:
    def reformat(self, s: str) -> str:
        counter = collections.defaultdict(list)
        
        for x in s:
            if x.isdigit():
                counter['number'].append(x)
            else:
                counter['alpha'].append(x)
        
        if abs(len(counter['number'])-len(counter['alpha'])) > 1:
            return ""

        d = sorted(counter.items(), key=lambda x: len(x[1]))

        res = ""
        d1 = d[0][1]
        d2 = d[1][1]
        
        while 1:
            if d2:
                res += d2.pop()
            if d1:
                res += d1.pop()
            
            if not d1 and not d2:
                break
        
        return res