# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        forwardSub = set()
        for i in range(len(s)-1):
            if s[i] == s[i+1] or s[i+1]+s[i] in forwardSub:
                return True
            forwardSub.add(s[i:i+2])

        return False
