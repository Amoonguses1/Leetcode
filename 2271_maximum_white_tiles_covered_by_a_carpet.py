# Time: O(NlogN)
# Space: O(N)
# N = len(tiles)
from typing import List
from bisect import bisect_right


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        maxCover = 0
        starts, ends = zip(*tiles)
        dp = [0] * (len(tiles) + 1)
        for i in range(len(tiles)):
            dp[i+1] = dp[i] + ends[i] - starts[i] + 1
        for left in range(len(tiles)):
            end = starts[left] + carpetLen
            right = bisect_right(starts, end)
            cover = dp[right] - dp[left] - max(0, ends[right-1] - end + 1)
            maxCover = max(maxCover, cover)
        return maxCover
