# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans, cnt = 0, 0
        for ch in s:
            if ch == "E":
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt -= 1
        return ans
