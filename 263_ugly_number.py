# Time: O(logn)
# Space: O(1)


class Solution:
    def isUgly(self, n: int) -> bool:
        for div in 2, 3, 5:
            while n > 1 and n % div == 0:
                n //= div
        return n == 1
