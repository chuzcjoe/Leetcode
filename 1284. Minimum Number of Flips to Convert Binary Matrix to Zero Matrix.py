class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])
        
        def flip(s,x,y):
            direc = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]
            
            for dx, dy in direc:
                nx = x+dx
                ny = y+dy
                if nx < 0 or nx >=m or ny < 0 or ny >=n:
                    continue
                else:
                    s ^= 1 << (nx*n+ny)
            
            return s
        
        start = 0
        cnt = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                start += mat[i][j] * (2**cnt)
                cnt += 1
        
        q = collections.deque([start])
        seen = set()
        seen.add(start)
        step = 0
        
        while q:
            size = len(q)
            
            for _ in range(size):
                cur = q.popleft()
                if cur == 0:
                    return step
                
                for a in range(m):
                    for b in range(n):
                        t = flip(cur, a, b)
                        
                        if t not in seen:
                            seen.add(t)
                            q.append(t)
                
            step += 1
        
        return -1
                
                
        
        
        