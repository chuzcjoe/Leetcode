class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos_set = collections.defaultdict(set)
        self.output = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ext = val not in self.pos_set
        self.pos_set[val].add(len(self.output))
        self.output.append(val)
        return ext
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos_set: return False
        
        
        last_num = self.output.pop(-1)
        self.pos_set[last_num].remove(len(self.output))
        
        if val != last_num:
            remove_idx = self.pos_set[val].pop()
            self.output[remove_idx] = last_num
            self.pos_set[last_num].add(remove_idx)
        
        if not self.pos_set[val]: del self.pos_set[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.output)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
