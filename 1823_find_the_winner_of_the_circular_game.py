class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """Function to find the game winner
            Args:
                n(int): an integer which stands for
                    the number of participations
            Returns:
                int: the winner of the game
        """
        # Time: O(n)
        # Space: O(1)
        """
        res = 0
        for i in range(2,n+1):
            res = (res+k) % i
        return res + 1
        """
        # recursion
        # Time: O(n)
        # Space: O(n)
        if not n.isdecimal():
            raise ValueError("Invalid input")

        return self.dp(n, k) + 1

    def dp(self, n, k):
        if n == 1:
            return 0

        return (self.dp(n-1, k)+k) % n
