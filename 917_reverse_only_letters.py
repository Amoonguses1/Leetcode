# Time: O(N)
# Space: O(N)
# N = len(s)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = [ch for ch in list(s)[::-1] if ch.isalpha()]
        ans = ""
        pos = 0
        for i in range(len(s)):
            if s[i].isalpha():
                if pos == len(chars):
                    ans += s[i:]
                    break
                ans += chars[pos]
                pos += 1
            else:
                ans += s[i]
        return ans
