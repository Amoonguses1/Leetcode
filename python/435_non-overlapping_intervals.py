# time: O(NlogN)
# Space: O(N)
# N = len(intervals)
from typing import List
from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Function to calculate the minimum number of intervals you needed
            to remove to make non-overlapping intervals
            Args:
                intervals(List[List[int]]): each list sdtands for an interval
            Returns:
                int: how many intervals are removed to make non-overlapping
                    intervals.
        """
        intervals_sorted = sorted(intervals, key=itemgetter(1))
        passed = intervals_sorted[0][0] - 1
        answer = 0
        for li in intervals_sorted:
            if li[0] < passed:
                answer += 1
            else:
                passed = li[1]
        return answer
