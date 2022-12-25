# Time: O(N)
# Space: O(1)
# N = len(prices)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Function to calculate the profit of
            buying and selling stock
            Agrs:
                prices(List[int]): the price the stock
            Returns:
                int: the max profit
        """
        if not prices:
            return -1

        profit, min_price = 0, float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price-min_price)
        return profit
