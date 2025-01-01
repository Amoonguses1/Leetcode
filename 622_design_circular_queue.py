

class MyCircularQueue:

    def __init__(self, k: int):
        # Time: O(k)
        # Space: O(k)
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear+1) % len(self.queue)
        self.count += 1
        return True

    def deQueue(self) -> bool:
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            return False

        self.count -= 1
        self.front = (self.front+1) % len(self.queue)
        return True

    def Front(self) -> int:
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        # Time: O(1)
        # Space: O(1)
        if self.isEmpty():
            return -1

        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        # Time: O(1)
        # Space: O(1)
        return self.count == 0

    def isFull(self) -> bool:
        # Time: O(1)
        # Space: O(1)
        return self.count == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
