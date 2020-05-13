class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        MAX = max(candies)
        res = []
        
        for i in range(len(candies)):
            tmp = abs(MAX - candies[i])
            if tmp <= extraCandies:
                res.append(True)
            else:
                res.append(False)
        
        return res
        