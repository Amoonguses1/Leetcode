import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort solution
        # Time: O(NlogN+MlogM)
        # Space: O(M+N)
        # M = len(s), N = len(t)
        sortS = sorted(s)
        sortT = sorted(t)
        return sortS == sortT

    def isAnagram2(self, s: str, t: str) -> bool:
        # hash solution
        # Time: O(N+M)
        # Space: O(M+N)
        # M = len(s), N = len(t)
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)
        for key, val in counterS.items():
            if counterT[key] != val:
                return False

        return len(counterS) == len(counterT)
