class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        occurrence = collections.defaultdict(int)
        next_nums = collections.defaultdict(int)
        
        for num in nums:
            occurrence[num] += 1
        
        for num in nums:
            if occurrence[num] == 0:
                continue
            elif next_nums[num] > 0:
                next_nums[num+1] += 1
                next_nums[num] -= 1
            
            elif occurrence[num+1] > 0 and occurrence[num+2] > 0:
                next_nums[num+3] += 1
                occurrence[num+1] -= 1
                occurrence[num+2] -= 1
            else:
                return False
            
            occurrence[num] -= 1
        
        return True
        
        