# array solution
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.keyValues = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        # Time: O(N)
        # Space: O(N)
        # N = len(self.keyValues[self.hash(key)])
        idx = self.hash(key)
        li = self.keyValues[idx]
        found = False
        for i in range(len(li)):
            if li[i][0] == key:
                li[i] = (key, value)
                found = True
                break
        if not found:
            self.keyValues[idx].append((key, value))
        return

    def get(self, key: int) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(self.keyValues[self.hash(key)])
        idx = self.hash(key)
        for liKey, value in self.keyValues[idx]:
            if key == liKey:
                return value
        return -1

    def remove(self, key: int) -> None:
        # Time: O(N)
        # Space: O(1)
        # N = len(self.keyValues[self.hash(key)])
        idx = self.hash(key)
        for i in range(len(self.keyValues[idx])):
            if self.keyValues[idx][i][0] == key:
                self.keyValues[idx].pop(i)
                return
        return

    def hash(self, key: int) -> int:
        return key % self.size


# linked list solution
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None


class MyHashMap2:

    def __init__(self):
        self.size = 1000
        self.keyValues = [None] * self.size

    def put(self, key: int, value: int) -> None:
        # Time: O(N)
        # Space: O(N)
        # N is the number of node in self.keyValues[self.hash(key)]
        idx = self.hash(key)
        node = self.keyValues[idx]
        if node is None:
            self.keyValues[idx] = Node(key, value)
            return

        found = False
        while True:
            if node.key == key:
                node.val = value
                found = True
                break
            if node.next is None:
                break
            node = node.next
        if not found:
            node.next = Node(key, value)
        return

    def get(self, key: int) -> int:
        # Time: O(N)
        # Space: O(N)
        # N is the number of node in self.keyValues[self.hash(key)]
        idx = self.hash(key)
        node = self.keyValues[idx]
        while node:
            if node.key == key:
                return node.val

            node = node.next
        return -1

    def remove(self, key: int) -> None:
        # Time: O(N)
        # Space: O(N)
        # N is the number of node in self.keyValues[self.hash(key)]
        idx = self.hash(key)
        node = prev = self.keyValues[idx]
        if node is None:
            return

        if node.key == key:
            self.keyValues[idx] = node.next
            return

        node = node.next
        while node:
            if node.key == key:
                prev.next = node.next
                break
            node = node.next
            prev = prev.next
        return

    def hash(self, key: int) -> int:
        return key % self.size
