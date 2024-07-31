# Time: O(NlogN)
# Space: O(N)
# N = len(tokens)
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score, cur = 0, 0
        tokens.sort()
        left, right = 0, len(tokens)
        while left < right:
            if tokens[left] <= power:
                cur += 1
                score = max(cur, score)
                power -= tokens[left]
                left += 1
            elif cur > 0:
                right -= 1
                power += tokens[right]
                cur -= 1
            else:
                break
        return score
