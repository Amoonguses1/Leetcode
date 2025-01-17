# Time: O(N)
# Space: O(N)
# N = len(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        left, right = 0, len(sList) - 1
        vowels = set("aeiouAEIOU")

        while left < right:
            while left < right and sList[left] not in vowels:
                left += 1
            while left < right and sList[right] not in vowels:
                right -= 1

            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1

        return "".join(sList)
