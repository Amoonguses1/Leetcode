# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() or word.isupper() or word.islower()
