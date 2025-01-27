import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.keys = []

    def insert(self, val: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        if val in self.dict:
            return False

        self.dict[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        if val not in self.dict:
            return False

        last_key = self.keys[-1]
        self.dict[last_key] = self.dict[val]
        self.keys[self.dict[val]] = last_key
        self.keys.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        # Time: O(1)
        # Space: O(1)
        return random.choice(self.keys)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
