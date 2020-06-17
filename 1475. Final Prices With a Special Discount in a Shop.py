class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = prices[:]
        n = len(prices)
        
        for i, p in enumerate(prices):
            for j in range(i+1, n):
                if prices[j] <= p:
                    res[i] = p - prices[j]
                    break
        
        return res
            