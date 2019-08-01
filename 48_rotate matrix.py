class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        
        for i in range(n//2):
            
            for j in range(i,n-1-i):
                temp0 = matrix[i][j]
                temp1 = matrix[j][n-1-i]
                temp2 = matrix[n-1-i][n-1-j]
                temp3 = matrix[n-1-j][i]
                matrix[i][j] = temp3
                matrix[j][n-1-i] = temp0
                matrix[n-1-i][n-1-j] = temp1
                matrix[n-1-j][i] = temp2
        
            
        return matrix
            
            
            
        
        
