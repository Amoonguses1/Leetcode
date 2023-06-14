# Time: O(N)
# Space: O(1)
# N = len(nums)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Function to get maximum sum with the following condition
        Condition
            If you choose ith number from an array,
            you can't choose i-1th and i+1th number.

        Args:
            nums(List[int]): a list consist of integer

        Returns:
            int: the maximum sum
        """
        old, tmp = 0, 0
        for num in nums:
            old, tmp = tmp, max(old+num, tmp)
        return tmp
