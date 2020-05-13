class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        
        """
        Solution 1: backtrack (TLE)
        n = len(hats)
        
        def backtrack(path, i):
            nonlocal cnt
            
            if i > n:
                return
            
            if len(path) == n:
                cnt += 1
                return
            
            for h in hats[i]:
                if h in path:
                    continue
                
                path += [h]
                backtrack(path[:], i+1)
                path = path[:-1]
        
        cnt = 0
        backtrack([],0)
        return cnt % (10**9 + 7)
        """
        
        """
        Solution 2: mask bit
        """
 
        n, mod = len(hats), 10**9+7
        a = collections.defaultdict(list)
        
        
        for i in range(n):
            for h in hats[i]:
                a[h].append(i)
        
        target = (1<<n)
        dp = [0] * target
        dp[0] = 1
        
        for hat in a:
            for i in range(target-1,-1,-1):
                for p in a[hat]:
                    if (i>>p)&1:
                        dp[i] += dp[i-(1<<p)]
                        dp[i] %= mod
        
        return dp[-1] % mod
        
        
        
            
            