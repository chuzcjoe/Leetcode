class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        if n == 1:
            return []
        
        #{0.333:'1/3'}
        dic = collections.defaultdict(str)
        
        nu = [i for i in range(1,n)]
        de = [i for i in range(2,n+1)]
        
        for n in nu:
            for d in de:
                if n >= d:
                    continue
                if n/d not in dic:
                    dic[n/d] = str(n)+'/'+str(d)
        
        res = []
        for k,v in dic.items():
            res.append(v)
        
        return res
        
        