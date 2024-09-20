# Time: O(N + MlogM)
# Space: O(N+M)
# N = len(word), M is the number of characters
import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        chCount = collections.Counter(word)
        nums = sorted(chCount.values())
        ans = 0
        for i in range(len(nums)):
            ans += nums[len(nums)-i-1] * (i//8 + 1)
        return ans
