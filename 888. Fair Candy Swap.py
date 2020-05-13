class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        diff = sum(A) - sum(B)
        
        target = diff // 2
        A = set(A)
        
        for b in set(B):
            if b+target in A:
                return [b+target, b]