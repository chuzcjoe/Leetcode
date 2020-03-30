class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        n= len(A)
        """
        odd = []
        even = []
        
        for i in range(n):
            if i % 2 == 0:
                odd.append([A[i],i])
            else:
                even.append([A[i],i])
        
        odd_idx = None
        even_idx = None
        
        for i in range(n//2):
            if odd[i][0] % 2:
                odd_idx = i
            
            if even[i][0] % 2 == 0:
                even_idx = i
                
            if odd_idx is not None and even_idx is not None:
                odd[odd_idx][0], even[even_idx][0] =  even[even_idx][0], odd[odd_idx][0]
                odd_idx = None
                even_idx = None
        
        res = []
        for i in range(n//2):
            res.append(odd[i][0])
            res.append(even[i][0])
        
        return res
        """
        
        i = 0
        j = 1
        
        while i < n and j < n:
            if A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
            else:
                A[i], A[j] = A[j], A[i]
        
        return A
        
                
            
        