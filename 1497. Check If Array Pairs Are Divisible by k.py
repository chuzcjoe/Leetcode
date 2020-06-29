class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        for i,a in enumerate(arr):
            arr[i] = a % k
        
        dic = collections.defaultdict(list)
        cnt = 0
        
        for j,n in enumerate(arr):
            if k-n in dic:
                cnt += 1
                dic[k-n].pop(0)
                if not dic[k-n]:
                    del dic[k-n]
            elif n == 0 and 0 in dic:
                cnt += 1
                dic[0].pop(0)
                if not dic[0]:
                    del dic[0]
            else:
                dic[n].append(j)
        
        print(cnt)
        return True if cnt == len(arr) // 2 else False
                