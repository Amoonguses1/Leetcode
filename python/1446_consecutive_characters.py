# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def maxPower(self, s: str) -> int:
        ans, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        return max(cur, ans)
