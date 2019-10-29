class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = self.nums.count(target)
        li = range(1,count+1)
        b = random.choice(li)
        
        met = 0
        for i,val in enumerate(self.nums):
            if val == target:
                met += 1
                if met == b:
                    return i
                else:
                    continue
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)