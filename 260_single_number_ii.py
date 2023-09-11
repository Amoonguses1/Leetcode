# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        p, q = 0, 0
        for num in nums:
            p ^= num
        for num in nums:
            if ((p & -p) & num) == 0:
                q ^= num
        return [p ^ q, q]
