from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Function to find  the fewest number of coins
            that you need to make up that amount.
            Args:
                coins(List[int]): an integer array of coins
                    representing coins of different denominations
                amount(int): a total amount of money
            Returns:
                int: the fewest number of coins
                    that you need to make up that amount.
        """
        # DP
        # Time: O(N)
        # Space: O(N)
        """
        if amount < 0:
            return -1
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == amount + 1:
            return -1

        else:
            return dp[amount]
        """
        if amount < 0:
            return -1
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
