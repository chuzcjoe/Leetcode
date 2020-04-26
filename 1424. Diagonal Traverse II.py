class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        res = []
        
        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                if len(res) <= i+j:
                    res.append([])
                res[i+j].append(x)
        
        out = []
        
        for row in res:
            for x in reversed(row):
                out.append(x)
        
        return out
                    
            
        