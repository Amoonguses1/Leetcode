

class Solution:
    def minimumPushes(self, word: str) -> int:
        # mathmatical
        # Time: O(1)
        # Space: O(1)
        d, m = divmod(len(word), 8)
        return 4 * d * (d+1) + m * (d+1)

    def minimumPushes2(self, word: str) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(word)
        ans = 0
        length = len(word)
        while length > 0:
            ans += length
            length -= 8
        return ans
