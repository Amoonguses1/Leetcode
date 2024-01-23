# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency = {}
        longestSubstring = 0
        for right, ch in enumerate(s):
            if ch not in frequency:
                frequency[ch] = 0
            frequency[ch] += 1
            windowLength = right - left + 1
            if windowLength - max(frequency.values()) <= k:
                longestSubstring = windowLength
            else:
                frequency[s[left]] -= 1
                left += 1
        return longestSubstring
