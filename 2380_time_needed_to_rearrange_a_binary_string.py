

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # Time: O(N)
        # Space: O(1)
        # N = len(s)
        ans = prefix = prev = 0
        for i, ch in enumerate(s):
            if ch == "1":
                ans = max(prev, i-prefix)
                prefix += 1
                if ans:
                    prev = ans + 1
        return ans

    def secondsToRemoveOccurrences2(self, s: str) -> int:
        # Time: O(N^2)
        # Space: O(N)
        # N = len(s)
        cnt = -1
        next_string = s
        s = ""
        while s != next_string:
            s = next_string
            next_string = ""
            pos = 0
            while pos < len(s):
                if s[pos:pos+2] == "01":
                    next_string += "10"
                    pos += 2
                else:
                    next_string += s[pos]
                    pos += 1
            cnt += 1
        return cnt
