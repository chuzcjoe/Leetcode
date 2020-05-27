class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        h = [[0] * c for _ in range(r)]
        v = [[0] * c for _ in range(r)]
        
        res = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]: 
                    h[i][j] = 1 if j == 0 else h[i][j-1]+1
                    v[i][j] = 1 if i == 0 else v[i-1][j] +1
        
        for i in range(r):
            for j in range(c):
                tmp = min(h[i][j], v[i][j])
                while tmp > res:
                    if tmp <= h[i-tmp+1][j] and tmp <= v[i][j-tmp+1]:
                        res = tmp
                    tmp -= 1
        
        return res ** 2
                