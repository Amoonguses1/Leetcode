# Time: O(max(N, log_10(k)))
# Space: O(max(N, log_10(k)))
# N = len(num)
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k, num[i] = divmod(num[i]+k, 10)
        if k:
            num = [int(digit) for digit in str(k)] + num
        return num
