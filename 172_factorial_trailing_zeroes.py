# Time: O(logn)
# Space: O(1)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Function to return the number of trailing zeroes in n!

        Args:
            n(int): an integer

        Returns:
            int: the number of trailing zeroes in n!
        """
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros
