# Time: O(1)
# Space: O(1)


class Solution:
    def minMovesToCaptureTheQueen(
            self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        if a == e and not (a == c and min(b, f) < d < max(b, f)):
            return 1

        if b == f and not (b == d and min(a, e) < c < max(a, e)):
            return 1

        if abs(c - e) == abs(d - f):
            if abs(a - c) == abs(b - d) and (b - f) * (b - d) < 0:
                return 2
            return 1

        return 2
