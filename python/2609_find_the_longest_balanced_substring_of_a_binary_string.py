# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        zeros, ones, before = 0, 0, ""
        for ch in s:
            if before != ch and ch == "0":
                ans = max(ans, min(zeros, ones))
                zeros, ones = 0, 0
            if ch == "0":
                zeros += 1
            else:
                ones += 1
            before = ch
        if zeros != 0:
            ans = max(ans, min(zeros, ones))
        return ans * 2
