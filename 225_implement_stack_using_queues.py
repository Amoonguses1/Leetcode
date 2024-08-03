

class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # Time: O(1)
        # Space: O(1)
        self.stack.append(x)

    def pop(self) -> int:
        # Time: O(1)
        # Space: O(1)
        return self.stack.pop()

    def top(self) -> int:
        # Time: O(1)
        # Space: O(1)
        return self.stack[-1]

    def empty(self) -> bool:
        # Time: O(1)
        # Space: O(1)
        return len(self.stack) == 0
