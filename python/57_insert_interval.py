# Time: O(N)
# Space: O(N)
# N = len(intervals)
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        """Function to insert newInterval to intervals
            Args:
                intervals(List[List[int]]): an array of non-overlapping
                    intervals
                newInterval(List[int]): an list which stands for an interval
            Returns:
                List[List[int]]: an array of non-overlapping intervals
        """
        s, e = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right
