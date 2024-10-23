# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for ch in n:
            ans = max(ans, int(ch))
        return ans
