class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def remove(L, ele):
            for i in range(L.count(ele)):
                L.remove(ele)
            
            return L
          
        
        res = []
        for i in range(len(arr2)):
            res.extend([arr2[i]] * arr1.count(arr2[i]))
            arr1 = remove(arr1, arr2[i])
        
        arr1.sort()
        for x in arr1:
            res.append(x)
        
        return res
        