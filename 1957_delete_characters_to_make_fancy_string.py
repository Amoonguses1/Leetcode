# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt, ans = 0, ""
        for i, ch in enumerate(s):
            if i > 0 and ch == s[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                ans += ch
        return ans
