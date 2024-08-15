# Time: O(N)
# Space: O(1)
import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = collections.Counter(s)
        odds = 0
        for val in count.values():
            if val % 2:
                odds += 1
        return odds <= k
