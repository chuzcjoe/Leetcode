class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        """
        Solution 1: O(N^3)
        #dp[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
        dp = [0] * (len(arr)+1)
        dp[1] = arr[0]
        res = 0
        
        for i,a in enumerate(arr[1:]):
            dp[i+2] = dp[i+1] ^ a
        
        
        for k in range(1, len(arr)):
            for i in range(0, k):
                j = i+1
                while j <= k:
                    if dp[i]^dp[j] == dp[k+1] ^ dp[j]:
                        res += 1
                    
                    j += 1
        
        return res
        
        """
        
        """
        Solution 2:
        """
        arr.insert(0, 0)
        n = len(arr)
        for i in range(n - 1):
            arr[i + 1] ^= arr[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res