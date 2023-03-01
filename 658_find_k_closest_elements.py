# Time: O(nlon)
# Space: O(1)
# n = len(arr)
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Function to return the k closest integers to x in the array.
        An integer a is closer to x than an integer b if:
        |a - x| < |b - x|, or
        |a - x| == |b - x| and a < b

        Args:
            arr(List[int]): a list consist of integers
            k(int): an integer 0 < k < arr.length
            x(int): a target integer

        Returns:
            List[int]: the k closest integers list
        """
        if x < arr[0]:
            return arr[:k]

        if x > arr[-1]:
            return arr[-k:]

        left, right = -1, len(arr)-k
        while left < right - 1:
            m = (left+right) >> 1
            if x - arr[m] > arr[m+k] - x:
                left = m
            else:
                right = m
        return arr[left+1:left+1+k]
