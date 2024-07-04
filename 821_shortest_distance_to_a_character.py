# Time: O(N)
# Space: O(N)
# N = len(s)
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [0] * len(s)
        prev = None
        for i, ch in enumerate(s):
            if ch == c:
                start = 0 if prev is None else (i+prev) // 2 + 1
                ans[start:i+1] = range(i-start, -1, -1)
                prev = i
            elif prev is not None:
                ans[i] = i - prev
        return ans
