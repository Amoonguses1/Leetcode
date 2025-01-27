# Time: O(N)
# Space: O(1)
# N = len(s)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt, ans = 0, 0
        vowels = "aeiou"
        for i in range(len(s)):
            if i >= k and s[i-k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
                ans = max(ans, cnt)
        return ans
