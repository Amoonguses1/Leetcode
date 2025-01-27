# Time: O(M+N)
# Space: O(M+N)
# M = len(s), N = len(target)
import collections


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sDict = collections.Counter(s)
        targetDict = collections.Counter(target)
        cnt = []
        for ch in targetDict:
            if ch in sDict:
                count = sDict[ch] // targetDict[ch]
                cnt.append(count)
            else:
                cnt.append(0)
                break
        return min(cnt)
