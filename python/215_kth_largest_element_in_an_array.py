# Time: O(NlogN)
# Space: O(N)
# N = len(nums)
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        """Function to find kth largest element in the array
            Args:
                nums(List[int]): an integer array
                k(int): an integer
            Returns:
                int: the kth element
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
