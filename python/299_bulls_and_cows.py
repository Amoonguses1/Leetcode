# Time: O(n)
# Space: O(1)
import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_s = collections.Counter(secret)
        count_g = collections.Counter(guess)
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows = 0
        for key, val in count_s.items():
            if key in count_g:
                cows += min(val, count_g[key])
        return str(bulls) + "A" + str(cows-bulls) + "B"
