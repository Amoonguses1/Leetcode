from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.operations = []

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        # Time: O(1)
        # Space: O(1)
        self.operations.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(self.operations)
        for row1, col1, row2, col2, val in reversed(self.operations):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return val
        return self.rectangle[row][col]
