# Time: O(n)
# Space: O(1)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur, old = 1, 0
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans += min(cur, old)
                old = cur
                cur = 1
        ans += min(cur, old)
        return ans
