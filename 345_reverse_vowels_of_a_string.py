# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        li = list(s)
        left, right = 0, len(li) - 1
        m = "aeiouAEIOU"
        while left < right:
            if li[left] in m and li[right] in m:
                li[left], li[right] = li[right], li[left]
                left += 1
                right -= 1
            elif li[left] not in m:
                left += 1
            elif li[right] not in m:
                right -= 1
        return "".join(li)
