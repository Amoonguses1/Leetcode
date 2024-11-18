# Time: O(N)
# Space: O(N)
# N = len(code)
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0] * length

        res = []
        code = code * 2

        if k > 0:
            curSum = sum(code[1:k+1])
            for i in range(length):
                res.append(curSum)
                curSum += code[i+k+1] - code[i+1]
            return res

        curSum = sum(code[length+k:length])
        for i in range(length):
            res.append(curSum)
            curSum += code[length+i] - code[length+k+i]
        return res
