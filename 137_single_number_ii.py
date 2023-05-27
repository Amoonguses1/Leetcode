# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Function to find single element

        Args:
            nums(List[int]): a list consist of integer
            every element appears three times except on

        Returns:
            int: single element
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ ones
        return ones
