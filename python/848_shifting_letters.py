# Time: O(N)
# Space: O(N)
# N = len(s)
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ""
        shift = sum(shifts)
        for i, num in enumerate(shifts):
            ans += chr(((ord(s[i])-ord("a")+shift) % 26) + ord("a"))
            shift -= num
        return ans
