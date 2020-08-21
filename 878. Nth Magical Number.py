class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        
        lcm = A * B // math.gcd(A,B)
        
        cnt = lcm // A + lcm // B - 1
        
        i = N // cnt
        j = N % cnt
        
        
        def count(x, lcm):
            
            return x//A + x//B - x//lcm
        
        l, r = 0, A*B
        
        while l < r:
            mid = l + (r-l)//2
            
            c = count(mid, lcm)
            
            if c < j:
                l = mid + 1
            else:
                r = mid
        
        return (i * lcm + l) % (10**9+7)