class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        seen = set()
        q = [1]
        
        primes = [2,3,5]
        
        while n:
            
            a = heapq.heappop(q)
            
            for p in primes:
                m = a * p
                
                if m not in seen:
                    seen.add(m)
                    heapq.heappush(q, m)
            
            n -= 1
            if not n:
                return a