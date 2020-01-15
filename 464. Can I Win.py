class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        if (1+maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        
        if maxChoosableInteger >= desiredTotal:
            return True
        
        seen = {}
        
        def recursive(nums, desiredTotal):
            nums = tuple(nums)
            if nums[-1] >= desiredTotal:
                return True
            if nums in seen:
                return seen[nums]
            
            for i in range(len(nums)):
                if not recursive(nums[0:i]+nums[i+1:], desiredTotal-nums[i]):
                    seen[nums] = True
                    return True
            
            seen[nums] = False
            return False
        
        return recursive(range(1,maxChoosableInteger+1),desiredTotal)