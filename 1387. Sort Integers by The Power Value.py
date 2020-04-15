class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def power(num):
            step = 0
            while num != 1:
                if num & 1:
                    num = num * 3 + 1
                else:
                    num = num // 2
                
                step += 1
            
            return step
        
        res = collections.defaultdict(list)
        for i in range(lo, hi+1):
            res[power(i)].append(i)
        
        res = sorted(res.items(), key=lambda x: x[0])
        order = []
        for _, v in res:
            sorted(v)
            order.extend(v)
            
        return order[k-1]