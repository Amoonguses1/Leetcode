
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # strip and split solution
        # Time: O(N)
        # Space: O(N)
        # N = len(s)
        wordList = s.strip().split()
        if not wordList:
            return 0
        return len(wordList[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(s)
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                ans += 1
            elif ans != 0:
                return ans

        return ans
