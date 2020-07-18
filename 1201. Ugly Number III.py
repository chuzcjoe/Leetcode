class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        #counts = A//a+A//b+A//c-A//lcm(ab)-A//lcm(ac)-A//lcm(bc)+A//lcm(abc)
        
        def lcm(x,y):
            return x*y//math.gcd(x,y)
        
        def count(A,x,y,z,xy,xz,yz,xyz):
            ans = A//x+A//y+A//z
            ans -= A//xy+A//xz+A//yz
            ans += A//xyz
            
            return ans
        
        lo = 1
        hi = 10**18
        ab = lcm(a,b)
        ac = lcm(a,c)
        bc = lcm(b,c)
        abc = lcm(ab, c)
        while lo < hi:
            mid = (lo+hi) // 2
            
            if count(mid, a, b, c, ab, ac, bc, abc) < n:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
                
        