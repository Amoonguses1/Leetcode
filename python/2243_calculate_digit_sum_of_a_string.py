# Time: O(NlogN)
# Space: O(N)
# N = len(s)


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            num = 0
            cur = ""
            for i in range(len(s)):
                if i != 0 and i % k == 0:
                    cur += str(num)
                    num = 0
                num += int(s[i])
            cur += str(num)
            s = cur
        return s
