# Time: O(n)
# Space:O(N)
# n = len(s1), N = len(s2)
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, length = Counter(s1), len(s1)
        stMatch = 0

        for i in range(len(s2)):
            if s2[i] in counter:
                if not counter[s2[i]]:
                    stMatch -= 1
                counter[s2[i]] -= 1
                if not counter[s2[i]]:
                    stMatch += 1
            if i >= length and s2[i-length] in counter:
                if not counter[s2[i-length]]:
                    stMatch -= 1
                counter[s2[i-length]] += 1
                if not counter[s2[i-length]]:
                    stMatch += 1
            if stMatch == len(counter):
                return True

        return False
