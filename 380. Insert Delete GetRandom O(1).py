class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set  = []
        self.dict = {}
        self.idx = -1

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.idx += 1
            self.dict[val] = self.idx
            self.set.append(val)
            
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            index = self.dict[val]
            self.dict[self.set[-1]] = index
            self.set[index] = self.set[-1]
            
            del self.set[-1]
            del self.dict[val]
            
            self.idx -= 1
            return True
        else:
            return False
            
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        choi = random.choice(range(0,self.idx+1))
        return self.set[choi]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()