# Time: O(n)
# Space: O(n)
# n = len(s)


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sDict = {}
        for i, ch in enumerate(s):
            sDict[ch] = i
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(sDict[ch]-i)

        return ans
