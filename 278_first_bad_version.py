# time: O(logn)
# space: O(1)
from typing import List


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n + 1
        while left < right - 1:
            now = (left + right) // 2
            if isBadVersion(now):
                right = now
            else:
                left = now
        return right
