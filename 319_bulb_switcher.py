# Time: O(1)
# Space: O(1)
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))
