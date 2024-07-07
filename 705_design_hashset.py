

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.li = [None] * self.size

    def add(self, key: int) -> None:
        # Time: O(N)
        # Space: O(N)
        # N = len(self.li[idx])
        idx = self.hash(key)
        if self.li[idx]:
            if key in self.li[idx]:
                return

            self.li[idx].append(key)
        else:
            self.li[idx] = [key]

    def remove(self, key: int) -> None:
        # Time: O(N)
        # Space: O(N)
        # N = len(self.li[idx])
        idx = self.hash(key)
        if self.li[idx] and key in self.li[idx]:
            self.li[idx].remove(key)

    def contains(self, key: int) -> bool:
        # Time: O(N)
        # Space: O(N)
        # N = len(self.li[idx])
        idx = self.hash(key)
        if self.li[idx] and key in self.li[idx]:
            return True
        return False

    def hash(self, key):
        return key % self.size


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
