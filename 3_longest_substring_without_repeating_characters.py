# Time: O(N)
# Space: O(N)
# N = len(s)
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Function to return the length of substring without
            repeating characters

            Args:
                s(str): a string

            Returns:
                int: the length of substring without repeating characters
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string.")

        # use dictionary
        """
        ans, start = 0, 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            ans = max(ans, i-start+1)
        return ans
        """
        # use deque
        ans = 0
        stack = deque()
        for ch in s:
            if ch in stack:
                while ch in stack:
                    stack.popleft()
            stack.append(ch)
            ans = max(len(stack), ans)
        return ans
