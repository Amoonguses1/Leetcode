# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(
        self,
        hours: List[int],
        target: int
    ) -> int:
        ans = 0
        for hour in hours:
            if hour >= target:
                ans += 1
        return ans
