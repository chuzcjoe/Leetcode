class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        nums = set()
        i = 0
        
        while 2**i <= 10**9:
            s = "".join(sorted(str(2**i)))
            nums.add(s)
            i += 1
        
        N = "".join(sorted(str(N)))
        
        if N in nums:
            return True
        else:
            return False
        
        