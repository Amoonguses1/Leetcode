from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(nums)
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Time: O(logk)
        # Space: O(logk)
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
