from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len( nums )
        flag = 0
        while flag < 1:
            if left == right - 1 or left == right:
                flag += 1
            now = (right + left ) // 2
            if nums[ now ] == target:
                return now
            elif nums[ now ] < target:
                left = now
            else:
                right = now
        return right