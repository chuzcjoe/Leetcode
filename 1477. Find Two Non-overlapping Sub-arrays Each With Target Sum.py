class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        #{prefix sum: idx}
        prefix = {0:-1}
        s = 0
        res = []
        
        for i,a in enumerate(arr):
            s += a
            prefix[s] = i
            if s - target in prefix:
                res.append([prefix[s-target]+1,i])
        
        res = sorted(res, key=lambda x: x[1]-x[0]+1)
        
        if len(res) <= 1:
            return -1
        
        n1 = n2 = -1
        n1 = res[0][1]-res[0][0]+1
        right = res[0][1]
        left = res[0][0]
        
        for x,y in res[1:]:
            if x > right or y < left:
                n2 = y-x+1
                break
        
        if n2 == -1:
            return -1
        else:
            return n1+n2
        
        
        
                