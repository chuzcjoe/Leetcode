class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        r = len(A)
        c = len(A[0])
        flg = 0
        direct = [[-1,0],[1,0],[0,-1],[0,1]]
        stack = []
        steps = 0
        
        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c or A[i][j] != 1:
                return
            
            A[i][j] = 2
            stack.append([i,j])
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    dfs(i,j)
                    flg = 1
                    break
            
            if flg:
                break
        
        while stack:
            size = len(stack)
            
            for _ in range(size):
                x,y = stack.pop(0)
                for dx,dy in direct:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= r or new_y < 0 or new_y >= c or A[new_x][new_y] == 2:
                        continue
                    
                    if A[new_x][new_y] == 1:
                        return steps
                    
                    A[new_x][new_y] = 2
                    stack.append([new_x, new_y])
            steps += 1
                
                    
                    