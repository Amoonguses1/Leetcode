from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Function to find peak index
            such that nums[i-1] < nums[i] < nums[i+1]
            Args:
                grid(list[int]): list of integer
            Returns:
                int: peak index in the list
        """
        """
        # linear solution
        # time O (n)
        # space O(1)
        # n = len(arr)

        for i in range(len(arr)):
            if arr[i+1] < A[i]:
                return i

        """
        # binarysearch
        # time O(logn)
        # space O(1)
        # n = len(arr)

        left = -1
        right = len(arr)
        while left < right - 1:
            now = (left+right) // 2
            if arr[now] > arr[now+1]:
                right = now
            else:
                left = now
        return right
