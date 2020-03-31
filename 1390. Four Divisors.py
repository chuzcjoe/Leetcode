class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        res = 0
        
        for x in nums:
            cnt = 0
            div = set()
            for i in range(1, int(sqrt(x))+1):
                if x % i == 0:
                    div.add(i)
                    div.add(x//i)
                
                if len(div) > 4:
                    break
            
            if len(div) == 4:
                res += sum(div)
        
        return res