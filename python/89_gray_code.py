# Time: O(2 ^^ N)
# Space: O(2 ^^ N)
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """Function to generate n-bit code sequence

        Args:
            n(int): the integer 2 ^^ n is the smallest integer
            which is larger than any integer in n-bit code sequence

        Returns:
            List[int]: n-bit code sequence
        """
        bit, res = 1, [0]
        for _ in range(n):
            res += [i | bit for i in reversed(res)]
            bit <<= 1
        return res
