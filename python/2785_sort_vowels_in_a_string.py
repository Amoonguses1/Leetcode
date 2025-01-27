from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        # Time: O(NlogN)
        # Space: O(N)
        # N = len(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowel_string = []
        for ch in s:
            if ch in vowels:
                vowel_string.append(ch)
        vowel_string.sort()
        cnt = 0
        ans = []
        for ch in s:
            add = ch
            if ch in vowels:
                add = vowel_string[cnt]
                cnt += 1
            ans.append(add)
        return "".join(ans)

    def sortVowels2(self, s: str) -> str:
        # Time: O(N)
        # Space: O(N)
        # N = len(s)
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        freq = defaultdict(int)
        for ch in s:
            if ch in vowels:
                freq[ch] += 1
        pos = 0
        ans = []
        for ch in s:
            add = ch
            if ch in vowels:
                while freq[vowels[pos]] == 0:
                    pos += 1
                add = vowels[pos]
                freq[vowels[pos]] -= 1
            ans.append(add)
        return "".join(ans)
