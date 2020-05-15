class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        res = 0
        
        for right in range(1,len(prices)):
            
            while prices[left] > prices[right]:
                left += 1
            
            res = max(res, prices[right]-prices[left])
        
        return res