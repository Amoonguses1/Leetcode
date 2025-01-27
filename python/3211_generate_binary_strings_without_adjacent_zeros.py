# Time: O(n*2^^n)
# Space: O(n*2^^n)
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        for _ in range(n-1):
            nxt = []
            for s in res:
                if s[-1] != "0":
                    nxt.append(s+"0")
                nxt.append(s+"1")
            res = nxt
        return res
