# Time: O(N+M)
# Space: O(N+M)
# N = len(ransomNote), M = len(magazine)
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if ch in count:
                if count[ch] == 0:
                    return False
                count[ch] -= 1
            else:
                return False

        return True
