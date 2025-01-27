# Time: O(NlogN + M)
# Space: O(N)
# N = len(capacity), M = len(apple)
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        apples = sum(apple)
        for i in range(len(capacity)):
            if apples < 1:
                return i

            apples -= capacity[len(capacity)-i-1]
        return len(capacity)
