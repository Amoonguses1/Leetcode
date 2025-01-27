# Time: O(N)
# Space: O(N)
# N = len(words) = len(groups)
from typing import List


class Solution:
    def getLongestSubsequence(
            self,
            words: List[str],
            groups: List[int]
    ) -> List[str]:
        ans = []
        group = (groups[0] + 1) % 2
        for i in range(len(words)):
            if group != groups[i]:
                ans.append(words[i])
                group = (group + 1) % 2
        return ans
