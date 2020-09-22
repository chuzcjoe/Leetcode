class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        N = len(arr)
        n = N-1 if N % 2 == 0 else N
        ans = 0
        prefix = [0]
        
        for a in arr:
            s = prefix[-1] + a
            prefix.append(s)
        
        for i in range(1,n+1,2):
            for j in range(0,N-i+1):
                ans += prefix[j+i] - prefix[j]
        
        return ans
                
            