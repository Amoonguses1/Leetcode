# Time: O(N)
# Space: O(N)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_pos = {}
        for i, ch in enumerate(s):
            last_pos[ch] = i
        for i, ch in enumerate(s):
            if ch in stack:
                continue
            while stack and stack[-1] > ch and last_pos[stack[-1]] > i:
                _ = stack.pop()
            stack.append(ch)
        return "".join(stack)
