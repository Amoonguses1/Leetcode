# Time: O(Nk^2)
# Space: O(Nk)
# N = len(words), k = sum(len(words))/ N


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w)+1 for w in s)
