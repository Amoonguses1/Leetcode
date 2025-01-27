# Time: O(N)
# Space: O(N)
from typing import List
import collections


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate array by k steps

        Given an integer array nums, rotate the array to
        the right by k steps, where k is non-negative.
        The change is in-place.

        Args:
            nums(List[int]): an integer array
            k(int): a non-negative number

        Returns:
            None
        """
        n = len(nums)
        k = k % n
        li = collections.deque()
        for i in range(k):
            li.append(nums[(i+k) % n])
            nums[(i+k) % n] = nums[i]
        for i in range(n-k):
            li.append(nums[(2*k+i) % n])
            nums[(2*k+i) % n] = li.popleft()
