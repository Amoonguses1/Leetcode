

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        # n = len(s)
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern2(self, s: str) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        # n = len(s)
        repeat = ""
        for ch in s:
            flag = True
            cnt = 0
            repeat += ch
            for i in range(0, len(s), len(repeat)):
                if s[i:i+len(repeat)] != repeat:
                    flag = False
                    break
                cnt += 1
            if flag and cnt > 1:
                return True

            if len(repeat) > len(s) // 2:
                return False
