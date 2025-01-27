# Time: O(N)
# Space: O(N)
# N =len(nums)
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        seen, cur = set(), set()
        direction = 0
        for i, num in enumerate(nums):
            if i in seen:
                continue
            if num > 0:
                direction = 1
            else:
                direction = -1
            while direction*num > 0:
                nextPos = self.calcPos(i, num, len(nums))
                if i in cur:
                    if len(cur) > 1 and nextPos != i:
                        return True

                    break
                cur.add(i)
                i = nextPos
                num = nums[i]
            seen |= cur
            cur = set()
        return False

    def calcPos(self, i, num, offset):
        nextPos = i + num
        while nextPos < 0:
            nextPos += offset
        return nextPos % offset
