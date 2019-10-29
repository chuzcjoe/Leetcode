import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = nums
        self.can = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        num = []
        for _ in range(len(self.ori)):
            choi = random.choice(self.can)
            self.can.remove(choi)
            num.append(choi)
        self.can = num[:]
        return num
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()