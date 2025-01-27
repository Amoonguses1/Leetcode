# Time: O(N)
# Space: O(N/k)
# N = len(s)


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s), k):
            hashed = self.hashSubstring(s[i:i+k])
            res += (chr(hashed+ord("a")))
        return res

    def substringHash(self, s):
        hashed = 0
        for ch in s:
            hashed += ord(ch) - ord("a")
        return hashed % 26
