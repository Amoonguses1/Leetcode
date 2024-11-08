# Time: O(N)
# Space: O(N)
# N = len(boxes)
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pref, prefCnt, suf, sufCnt = 0, 0, 0, 0
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            res[i] += pref
            res[-i-1] += suf
            prefCnt += "1" == boxes[i]
            sufCnt += "1" == boxes[-i-1]
            pref += prefCnt
            suf += sufCnt
        return res
