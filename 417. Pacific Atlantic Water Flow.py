class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not matrix:
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        
        p_visited = [[0]*col for _ in range(row)]
        a_visited = [[0]*col for _ in range(row)]
        
        
        
        
        
        def bfs(matrix,visited,i,j):
            visited[i][j] = '*'
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for x,y in directions:
                cur_x = i + x
                cur_y = j + y
                if cur_x < 0 or cur_x >=row or cur_y < 0 or cur_y >= col or visited[cur_x][cur_y] == '*' or matrix[i][j] > matrix[cur_x][cur_y]:
                    continue
                bfs(matrix,visited,cur_x,cur_y)
        
            
        result = []
        for i in range(row):
            bfs(matrix,p_visited,i,0)
            bfs(matrix,a_visited,i,col-1)
        for i in range(col):
            bfs(matrix,p_visited,0,i)
            bfs(matrix,a_visited,row-1,i)
        
        for i in range(row):
            for j in range(col):
                if p_visited[i][j] == '*' and a_visited[i][j] == '*':
                    result.append([i,j])
                    
        return result
                