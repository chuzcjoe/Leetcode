class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def compute_sum(n):
            n = str(n)
            return sum([int(x) for x in n])
        
        res = collections.defaultdict(list)
        
        for i in range(1,n+1):
            res[compute_sum(i)].append(i)
        
        MAX_size = 0
        cnt = 0
        
        res_ordered = sorted(res.items(), key=lambda t: len(t[1]), reverse=True)
        # res now is list data type
        
        MAX_size = len(res_ordered[0][1])
        
        for k,v in res.items():
            if len(v) == MAX_size:
                cnt += 1
        
        return cnt
            
            