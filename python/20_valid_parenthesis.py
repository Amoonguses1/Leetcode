# Time: O(N)
# Space: O(N)
# N = len(s)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif len(stack) == 0 or dic[stack.pop()] != ch:
                return False
        return len(stack) == 0
