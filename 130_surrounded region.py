class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        
        def dfs(board,i,j):
            if i < 0 or i >= len(board) or j >= len(board[0]) or j < 0 or board[i][j] != 'O':
                return 
            
            board[i][j] = '#'
            
            dfs(board,i-1,j)
            dfs(board,i+1,j)
            dfs(board,i,j-1)
            dfs(board,i,j+1)
            
        #start from edges
        for i in range(len(board)):
            dfs(board,i,0)
            dfs(board,i,len(board[0])-1)
        
        for j in range(len(board[0])):
            dfs(board,0,j)
            dfs(board,len(board)-1,j)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return board
        