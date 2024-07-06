# Time: O(N)
# Space: O(1)
# N = max(len(a), len(b))


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return max(len(a), len(b))
