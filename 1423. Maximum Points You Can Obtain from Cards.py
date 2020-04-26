class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        n = len(cardPoints)
        
        slide = n - k
        cur_sum = sum(cardPoints[:n-k])
        res = cur_sum
        left = 0
        
        for right in range(n-k,n):
            print(right)
            cur_sum = cur_sum + cardPoints[right] - cardPoints[left]
            res = min(res, cur_sum)
            left += 1
        
            
        return sum(cardPoints) - res
            
        