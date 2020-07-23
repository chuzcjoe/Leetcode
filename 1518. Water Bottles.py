class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        if numBottles < numExchange:
            return numBottles
        
        ans = numBottles
        
        numfull = numBottles // numExchange
        empty = numBottles % numExchange
        
        while numfull+empty >= numExchange:
            ans += numfull
            total = numfull+empty
            print(numfull, empty)
            numfull = total // numExchange
            empty = total % numExchange
            
        
        return ans+numfull if numfull > 0 else ans
            
            