class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        t = sum(nums) % p
        
        if t == 0:
            return 0
        
        prefix = [0]
        dic = {0:0}
        res = len(nums)
        
        for a in nums:
            prefix.append(prefix[-1]+a)
        
        for i in range(1,len(prefix)):
            reminder = prefix[i] % p
            dic[reminder] = i
            
            if (reminder-t)%p in dic:
                res = min(res, i-dic[(reminder-t)%p])
            
        
        return -1 if res == len(nums) else res