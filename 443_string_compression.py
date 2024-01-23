# Time: O(N)
# Space: O(1)
# N = len(chars)
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans, pos = 0, 0
        while pos < len(chars):
            letter = chars[pos]
            count = 0
            while pos < len(chars) and chars[pos] == letter:
                count += 1
                pos += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for ch in str(count):
                    chars[ans] = ch
                    ans += 1
        return ans
