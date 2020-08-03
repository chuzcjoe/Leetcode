class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        
        ans = 0
        
        def findidx(arr):
            right = len(arr) - 1
            for i in range(right,-1,-1):
                if arr[i] == 1:
                    return right - i
            
            return right
        
        r = len(grid)
        c = len(grid[0])
        a = []
        
        for _,row in enumerate(grid):
            a.append(findidx(row))
        
        print(a)
        
        for j in range(r):
            target = r - j - 1
            if a[j] >= target:
                continue
            flag = False
            
            for k in range(j+1, r):
                if a[k] >= target:
                    ans += k-j
                    a[j+1:k+1] = a[j:k]
                    flag = True
                    break
                
            if not flag:
                return -1
        
        return ans
                
            
        
        
            
            
        
        