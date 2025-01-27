# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > 2:
                return False
        return True
