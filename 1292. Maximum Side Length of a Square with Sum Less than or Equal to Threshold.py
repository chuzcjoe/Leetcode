class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        DP = [[0]*len(mat[0]) for _ in range(len(mat))]
        #compute presum
        for a in range(len(mat)):
            for b in range(len(mat[0])):
                if a-1 <0 and b-1 < 0:
                    DP[a][b] = mat[a][b]
                elif a-1 < 0:
                    DP[a][b] = DP[a][b-1] + mat[a][b]
                elif b-1 < 0:
                    DP[a][b] = DP[a-1][b] + mat[a][b]
                else:
                    DP[a][b] = DP[a-1][b] + DP[a][b-1] + mat[a][b] - DP[a-1][b-1]
        
        print(DP)
        mid = 0
        l = 0
        r = min(len(mat), len(mat[0]))
        
        while l < r:
            mid = (l+r) // 2
            flg = False
            
            for i in range(len(mat)-mid):
                for j in range(len(mat[0])-mid):
                    p1 = DP[i+mid][j+mid]
                    p2 = DP[i+mid][j-1] if j >= 1 else 0
                    p3 = DP[i-1][j+mid] if i >= 1 else 0
                    p4 = DP[i-1][j-1] if i >= 1 and j >= 1 else 0
                    
                    SUM = p1 - p2 - p3 + p4
                    
                    if SUM <= threshold:
                        flg = True
                        break
                
                if flg:
                    break
            
            if flg:
                l = mid + 1
            else:
                r = mid
            
        return l
                    
                    