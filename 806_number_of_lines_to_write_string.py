# Time: O(N)
# Space: O(1)
# N = len(s)
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        cnt = 0
        for ch in s:
            size = widths[ord(ch)-ord("a")]
            cnt += size
            if cnt > 100:
                lines += 1
                cnt = size
        return [lines, cnt]
