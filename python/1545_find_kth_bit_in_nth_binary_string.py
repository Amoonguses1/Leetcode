class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """ Function to find the kth character from
            the specific string
            Args:
                n(int): an integer
                k(int): an integer
            Returns:
                str: the kth character
        """
        if not isinstance(n, int) or not isinstance(k, int):
            raise ValueError("The needed input type is int.")

        if k > 2 ** n - 1:
            raise ValueError("k is too big.")

        # Time: O(1)
        # Space: O(1)
        """
        return str(k / (k & -k) >> 1 & 1 ^ k & 1 ^ 1)
        """
        # Time: O(logk)
        # Space: O(logk)
        ans = self.dp(n, k)
        if ans:
            return "0"

        return "1"

    def dp(self, n, k):
        if k == 1:
            return True

        if k == 2 ** (n-1):
            return False

        if k < 2 ** (n-1):
            return self.dp(n-1, k)

        return not self.dp(n-1, 2**n-k)
