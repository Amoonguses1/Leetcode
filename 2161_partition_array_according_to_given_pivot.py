# Time: O(N)
# Space: O(N)
# N = len(nums)
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pref, suf = [], []
        pivCnt = 0
        for num in nums:
            if num < pivot:
                pref.append(num)
            elif num == pivot:
                pivCnt += 1
            else:
                suf.append(num)
        return pref + [pivot] * pivCnt + suf
