# Time: O(N)
# Space: O(1)
# N = len(prices)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Function to calculate maximum profit you can achieve

        Args:
            prices(List[int]): prices[i] stands for a given stock price
            on the ith day

        Returns:
            int: the ma profit
        """
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total
