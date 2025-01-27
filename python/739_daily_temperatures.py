# Time: O(N)
# Space: O(N)
# N = len(temperatures)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, curTemperature in enumerate(temperatures):
            while stack and stack[-1][1] < curTemperature:
                pos, _ = stack.pop()
                ans[pos] = i - pos
            stack.append([i, curTemperature])
        return ans
