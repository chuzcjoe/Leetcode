class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        ans = [None] * len(s)
        
        for i,idx in enumerate(indices):
            ans[idx] = s[i]
        
        return "".join(ans)