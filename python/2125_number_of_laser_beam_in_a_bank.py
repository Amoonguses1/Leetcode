# Time: O(MN)
# Space: O(1)
# M = len(bank), N = len(bank[0])
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = prev = 0
        for s in bank:
            cnt = s.count('1')
            if cnt != 0:
                res += prev * cnt
                prev = cnt
        return res
