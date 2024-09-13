# Time: O(N)
# Space: O(N)
# N = len(code)
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        length = len(code)
        code = code * 2
        ans = []
        for i in range(length):
            if k > 0:
                ans.append(sum(code[i+1:i+k+1]))
            else:
                ans.append(sum(code[i+length+k:i+length]))
        return ans
