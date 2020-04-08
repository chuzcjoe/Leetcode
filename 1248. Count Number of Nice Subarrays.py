class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        res = left = 0
        cnt = 0
        
        counter = collections.Counter({"odd":0})
        
        for right in range(len(nums)):
            if nums[right] & 1:
                counter['odd'] += 1
                cnt = 0
            
            while counter['odd'] == k:
                cnt += 1
                if nums[left] & 1:
                    counter['odd'] -= 1
                left += 1
                
            res += cnt
            
        return res
            
            