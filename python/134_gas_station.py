# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Function to return the starting gas station's index
        if you can travel around the circuit once in the clockwise direction,
        otherwise return -1

        Args:
            gas(List[int]): the amount of gas available in the ith station
            cost(List[int]): the consuming amount of gas
            between ith station and i+1th station

        Returns:
            int: the start point of travel
        """
        if sum(gas) - sum(cost) < 0:
            return -1

        start, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
