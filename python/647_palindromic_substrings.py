# Time: O(N^2)
# Space: O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for center in range(len(s)):
            even = self.countPalin(s, center, center+1)
            odd = self.countPalin(s, center, center)
            ans += even + odd
        return ans

    def countPalin(self, s, left, right):
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            cnt += 1
        return cnt
