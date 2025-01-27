from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        self.sums = [0]
        cur = 0
        for num in nums:
            cur += num
            self.sums.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return self.sums[right+1] - self.sums[left]
