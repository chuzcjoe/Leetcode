class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr = sorted(arr)
        n = len(arr)
        mean = arr[(n-1)//2]
        
        tmp = []
        for a in arr:
            tmp.append([abs(a-mean),a])
            
        res = sorted(tmp, key=lambda x: (x[0], x[1]))
        
        return [v for _,v in res[::-1][:k]]
        
        