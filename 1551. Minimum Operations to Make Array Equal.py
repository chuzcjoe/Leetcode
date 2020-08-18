class Solution:
    def minOperations(self, n: int) -> int:
        
        if n&1:
            mid = n // 2
            mid_val = 2 * (mid) + 1
            return sum(mid_val-(2*i+1) for i in range(mid))
        else:
            mid = n // 2
            mid_val = 2 * mid
            return sum(mid_val-(2*i+1) for i in range(mid))