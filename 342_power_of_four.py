from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        if n <= 0:
            return False

        log_base4 = log(n) / log(4)
        return log_base4 == int(log_base4)

    def isPowerOfFour2(self, n: int) -> bool:
        # Time: O(logN)
        # Space: O(1)
        if n <= 0:
            return False

        while n > 1:
            if n % 4:
                return False

            n //= 4
        return True
