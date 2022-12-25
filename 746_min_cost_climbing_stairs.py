# Time: O(N)
# Space: O(1)
# N = len(cost)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Function to calculate minimum cost
            Args:
                cost(List[int]): the cost which needs to climb up the stairs
            Returns:
                int: the minimum cost which needs to climb up from bottom to
                    top
        """
        cur, before = 0, 0
        length = len(cost) - 1
        for i in range(length):
            cur, before = min(cur+cost[i+1], before+cost[i]), cur
        return cur
