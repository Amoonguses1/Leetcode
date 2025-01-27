
# Time: O(NlogN)
# Space: O(N)
# N = len(intervals)
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        self.posDist = {}
        self.startList = []
        for i, interval in enumerate(intervals):
            self.posDist[interval[0]] = i
            self.startList.append(interval[0])
        self.startList.sort()
        ans = []
        for _, end in intervals:
            ans.append(self.binarySearch(end))
        return ans

    def binarySearch(self, end):
        if end > self.startList[-1]:
            return -1

        left, right = -1, len(self.startList)
        while right - left > 1:
            mid = (left+right) // 2
            if self.startList[mid] < end:
                left = mid
            else:
                right = mid
        return self.posDist[self.startList[right]]
