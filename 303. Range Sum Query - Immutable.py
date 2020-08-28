class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        
        s = 0
        for a in nums:
            s += a
            self.prefix.append(s)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j+1] - self.prefix[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)