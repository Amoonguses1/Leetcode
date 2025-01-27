# Time: O(N)
# Space: O(1)
# N is the number of digits on given integer


class Solution:
    def reverse(self, x: int) -> int:
        """Function to return the given numbers its digits reversed.
            If digits-reversed integer is outside of the 32-bit range,
            return 0

        Args:
            x(int): a signed 32-bit integer

        Returns:
            int: a 32-bit digits-reversed integer
        """
        res = 0
        sign = 1
        if x < 0:
            sign = -1
        x *= sign
        while x > 0:
            res *= 10
            res += x % 10
            x //= 10
        if res > pow(2, 31):
            return 0

        res *= sign
        return res
