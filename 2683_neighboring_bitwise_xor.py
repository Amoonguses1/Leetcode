# Time: O(N)
# Space: O(1)
# N = len(derived)


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        candidate = 0
        for binary in derived:
            candidate ^= binary
        return candidate == 0
