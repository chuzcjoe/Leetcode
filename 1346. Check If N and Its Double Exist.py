class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        #Similar to two sum
        
        dic = collections.defaultdict(int)
        
        for a in arr:
            if dic[a]>=1:
                return True
            
            if a % 2 == 0:
                dic[a//2] += 1
            
            dic[a*2] += 1
        
        return False