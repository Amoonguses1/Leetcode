# Time: O(n^2)
# Space: O(n^2)
from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(1, n+1):
            cur = []
            for j in range(i):
                if j == 0 or j == i-1:
                    cur.append(1)
                else:
                    curNum = ans[-1][j-1] + ans[-1][j]
                    cur.append(curNum)
            ans.append(cur)
        return ans
