class LRUCache:

    def __init__(self, capacity: int):
        
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        v = self.dict.pop(key)
        self.dict[key] = v
        
        return v
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            #update
            self.dict[key] = value
        else:
            if self.remain > 0:
                self.dict[key] = value
                self.remain -= 1
            else:
                #pop first item
                self.dict.popitem(last=False)
                self.dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)