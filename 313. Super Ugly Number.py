class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        seen = set()
        q = [1]
        
        while n:
            
            a = heapq.heappop(q)
            
            for p in primes:
                m = p*a
                if m not in seen:
                    seen.add(m)
                    heapq.heappush(q,m)
            
            n -= 1
        
        return a
        