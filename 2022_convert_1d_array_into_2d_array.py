# Time: O(N)
# Space: O(N)
# N = len(original)
from typing import List


class Solution:
    def construct2DArray(
            self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        if len(original) != m * n:
            return []

        newArr = []
        for i in range(0, len(original), n):
            newArr.append(original[i:i+n])
        return newArr
