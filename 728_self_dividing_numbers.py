# Time: O(N(log_10 N) )
# Space: O(1)
# N = right
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            num = str(i)
            isSelfDiv = True
            if "0" in num:
                continue
            for ch in num:
                j = int(ch)
                if i % j != 0:
                    isSelfDiv = False
                    break
            if isSelfDiv:
                ans.append(i)
        return ans
