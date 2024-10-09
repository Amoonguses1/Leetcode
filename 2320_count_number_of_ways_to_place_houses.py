# Time: O(n)
# Space: O(1)


class Solution:
    def countHousePlacements(self, n: int) -> int:
        pprev, prev = 1, 1
        modulo = (pow(10, 9)+7)
        for _ in range(n):
            prev, pprev = (pprev + prev) % modulo, prev
        return pow(prev, 2, modulo)
