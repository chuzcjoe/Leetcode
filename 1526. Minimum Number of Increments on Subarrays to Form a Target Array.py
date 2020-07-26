class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        ans = target[0]
        
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i]-target[i-1]
        
        return ans