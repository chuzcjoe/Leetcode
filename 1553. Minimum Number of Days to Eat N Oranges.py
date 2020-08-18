class Solution:
    def minDays(self, n: int) -> int:
        
        """
        #1. naive dp: LTE
        dp = [1] * (n+1)
        
        for i in range(2, n+1):
            if i % 2 == 0 and i % 3 == 0:
                dp[i] = min(dp[i-1], dp[i-i//2], dp[i-2*(i//3)]) + 1
            elif i % 2 == 0:
                dp[i] = min(dp[i-1], dp[i-i//2]) + 1
            elif i % 3 == 0:
                dp[i] = min(dp[i-1], dp[i-2*(i//3)]) + 1
            else:
                dp[i] = dp[i-1] + 1
        
        return dp[-1]
        """
        
        #2. advanced dp
        
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return n
            
            return 1+min(n%2+dp(n//2), n%3+dp(n//3))
        
        return dp(n)
        
        """
        3. BFS
        
        deque = collections.deque([n])
        steps = 0
        seen  = set()
        seen.add(n)
        
        while True:
            size = len(deque)
            for _ in range(size):
                x = deque.popleft()
                if x == 0:
                    return steps
                
                if x % 3 == 0 and x//3 not in seen:
                    deque.append(x//3)
                    seen.add(x//3)
                
                if x % 2 == 0 and x//2 not in seen:
                    deque.append(x//2)
                    seen.add(x//2)
                
                if x-1 not in seen:
                    deque.append(x-1)
                    seen.add(x-1)
            
            steps += 1
        """
        
                
            
        
        
        