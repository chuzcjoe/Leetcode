class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        #target = [1,2,3,4], arr = [2,4,1,3]
        c1 = collections.Counter(target)
        c2 = collections.Counter(arr)
        
        for k in c1.keys():
            if c1[k] != c2[k]:
                return False
        
        return True
                                    