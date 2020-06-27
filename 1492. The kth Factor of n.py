class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        f = []
        
        for i in range(1, n+1):
            if n % i == 0:
                f.append(i)
        
        print(f)
        return f[k-1] if k <= len(f) else -1