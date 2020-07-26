class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        dp_ones = [0] * len(arr)
        dp_zeros = [0] * len(arr)
        
        
        for i in range(len(arr)):
            arr[i] = arr[i] % 2
        
        for j,a in enumerate(arr):
            if j == 0:
                dp_ones[j] = 1 if a % 2 == 1 else 0
                dp_zeros[j] = 1 if a % 2 == 0 else 0
                continue
            
            if a == 0:
                dp_zeros[j] = dp_zeros[j-1] + 1
                dp_ones[j] = dp_ones[j-1]
            
            elif a == 1:
                dp_zeros[j] = dp_ones[j-1]
                dp_ones[j] = dp_zeros[j-1] + 1
        
        return sum(dp_ones) % (10**9+7)