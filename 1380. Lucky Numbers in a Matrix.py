class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        for row in range(len(matrix)):
            
            MIN = min(matrix[row])
            idx = matrix[row].index(MIN)
            val = matrix[row][idx]
            if val == max([x[idx] for x in matrix]):
                res.append(val)
                
        
        return res