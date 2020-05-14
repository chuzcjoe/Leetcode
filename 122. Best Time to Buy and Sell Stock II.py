class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #valley_i peak_i valley_j peak_j
        #we always want to buy at valley_i and sell at next peak_i
        
        res = 0
        buy = sell = 0
        n = len(prices)
        
        while buy < n and sell < n:
            
            while buy < n-1 and prices[buy+1] < prices[buy]:
                buy += 1
            
            
            sell = buy
            
            while sell < n-1 and prices[sell+1] > prices[sell]:
                sell += 1
            
            res += prices[sell]-prices[buy]
            buy = sell + 1
        
        return res
        
        
        