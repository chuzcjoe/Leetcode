class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles = sorted(piles, reverse=True)
        ans = 0
        
        n = len(piles) // 3
        for i in range(0,2*n-1,2):
            ans += piles[i+1]
        
        return ans
        