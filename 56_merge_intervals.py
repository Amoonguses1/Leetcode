# TIme: O(NlogN)
# Space: O(N)
# N = len(intervals)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Function to merge overlapping intervals.
            Args:
                intervals(List[List[int]]): each List stands for an interval.
            Returns:
                List[List[int]]: an array of the non-overlapping intervals
        """
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged
