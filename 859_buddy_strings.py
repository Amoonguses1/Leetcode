# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(s) != len(set(s)):
            return True

        left, right = 0, len(s) - 1
        while left < right and s[left] == goal[left]:
            left += 1
        while right > 0 and s[right] == goal[right]:
            right -= 1
        if left >= right:
            return False
        swappedS = s[:left] + s[right] + \
            s[left+1:right] + s[left] + s[right+1:]
        return swappedS == goal
