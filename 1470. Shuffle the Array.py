class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        tmp2 = nums[n:]
        tmp1 = nums[:n+1]
        
        res = []
        
        for a,b in zip(tmp1, tmp2):
            res.append(a)
            res.append(b)
        
        return res