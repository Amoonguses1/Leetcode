class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """Function to find the character of the k-th integer of
            n-th string
            Args:
                n(int): an integer
                k(int): an integer
            Returns:
                int: an integer
        """
        # Time: O(logk)
        # Space: O(1)
        """
        res = 0
        k -= 1
        while k > 0:
            if k % 2:
                if res == 1:
                    res = 0
                else:
                    res = 1
            k //= 2
        if res == 0:
            return res

        return 1
        """
        # recursion
        # Time: O(n)
        # Space: O(n)
        if not n.isdecimal() or not k.isdecimal():
            raise ValueError("invalid input")

        return self.dp(n, k-1)

    def dp(self, n, k):
        if n == 1:
            return 0

        before = self.dp(n-1, k//2)
        if k % 2:
            if before == 0:
                return 1

            return 0

        else:
            return before
