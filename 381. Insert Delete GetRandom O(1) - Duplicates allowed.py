class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dict = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = 1
            self.nums.append(val)
            return True
        else:
            self.dict[val] += 1
            self.nums.append(val)
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            self.dict[val] -= 1
            if self.dict[val] == 0:
                del self.dict[val]
            self.nums.remove(val)
            return True
        else:
            False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()