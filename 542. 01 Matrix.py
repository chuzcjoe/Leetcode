class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        col = len(matrix[0])
        
        dis = [[0 for i in range(col)] for j in range(row)]
        
        def bfs(i,j):
            step = 0
            visited = set()
            visited.add((i,j))
            nodes = [(i,j)]
            
            if matrix[i][j] == 0:
                return 0
            
            while nodes:
                step += 1
                size = len(nodes)
                for s in range(size):
                    (i, j) = nodes.pop(0)
                    
                    for x, y in [[0,1],[0,-1],[1,0],[-1,0]]:
                        next_i, next_j = i+x, j+y
                        if 0 <= next_i < row and 0 <= next_j < col and (next_i, next_j) not in visited:
                            if matrix[next_i][next_j] == 0:
                                return step
                            
                            visited.add((next_i, next_j))
                            nodes.append((next_i, next_j))
                        else:
                            continue
            return step
        
        for i in range(row):
            for j in range(col):
                dis[i][j] = bfs(i,j)
        
        return dis
        