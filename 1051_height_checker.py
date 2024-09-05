from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Counting sort
        # Time: O(M+N)
        # Space: O(M)
        # M = maximum value of heights
        # N = len(heights)
        cntList = [0] * max(heights)
        for height in heights:
            cntList[height-1] += 1
        pos, cnt = 0, 0
        for height in heights:
            while cntList[pos] == 0:
                pos += 1
            if height != pos + 1:
                cnt += 1
            cntList[pos] -= 1
        return cnt

    def heightChecker2(self, heights: List[int]) -> int:
        # sort with built-in function
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(heights)
        sortedHeights = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                cnt += 1
        return cnt
