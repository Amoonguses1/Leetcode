import heapq
from typing import List


class Solution(object):
    _dp = [0]

    def numSquares(self, n):
        """Function to return the least number of perfect square numbers
        that sum to n
            Args:
                n(int): natural number
            Returns:
                int: the least number of perfect square numbers that sum to n
        """
        # static dp
        # this function calculate only when len(_dp) is smaller than n.
        # In other words, this function extends dp only when the new N
        # is larger than the length of the list.
        # Time: O(N*(3/2))
        # Space: O(N)
        """
        if n < 0:
            return

        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
        """
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square:
                        return d

                    if node < square:
                        break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1
