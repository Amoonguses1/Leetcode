# Time: O(1)
# Space: O(1)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """Function to return the bitwise AND of all numbers
        in range [left, right]
        Args:
            left(int): an integer
            right(int): an integer
            Constraints
                0 <= left <= right <= pow(2,31) - 1
        Returns:
            int: the bitwise AND of all numbers in range [left, right]
        """
        shift = len(str(bin(right-left)))-2
        mask = 2147483647 << shift
        return left & right & mask
