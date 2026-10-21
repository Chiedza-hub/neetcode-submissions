import random 

class RandomizedSet:

    def __init__(self):
        self.map_ = {}
        self.list_ = []
        
        

    def insert(self, val: int) -> bool:
        if val not in self.map_:
            self.map_[val] = len(self.list_)
            self.list_.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.map_:
            index = self.map_[val]
            lastVal = self.list_[-1]
            self.list_[index] = lastVal
            self.map_[lastVal] = index
            self.list_.pop()
            del self.map_[val]
            return True
        return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.list_)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()