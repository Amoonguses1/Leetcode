# Time: O(logn)
# Space: O(1)


class Solution:
    def lastRemaining(self, n: int) -> int:
        """Function to find the last number with the specific algorithm
            Args:
                n(int): a natural number
            Returns:
                int: the last number
        """
        if not n.isdecimal():
            raise ValueError("Invalid input. Input an integer")

        return self.recursion(n, True)

    def recursion(self, n, forward):
        if n == 1:
            return 1

        forward = not forward
        if forward and n % 2 == 0:
            return 2 * self.recursion(n//2, forward) - 1

        return 2 * self.recursion(n//2, forward)
