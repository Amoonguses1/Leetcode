# Time: O(N)
# Space: O(1)
# N = len(s)
from collections import defaultdict


class Solution:
    def originalDigits(self, s: str) -> str:
        countDict = defaultdict(lambda: 0)
        for ch in s:
            countDict[ch] += 1
        distinct = ["z", "w", "u", "x", "g", "o", "h", "f", "s", "i"]
        nums = [("zero", 0),
                ("two", 2),
                ("four", 4),
                ("six", 6),
                ("eight", 8),
                ("one", 1),
                ("three", 3),
                ("five", 5),
                ("seven", 7),
                ("nine", 9)
                ]
        numOfNum = dict([(num, 0) for num in range(10)])
        for i, ch in enumerate(distinct):
            numOfNum[nums[i][1]] = countDict[ch]
            for st in nums[i][0]:
                countDict[st] -= numOfNum[nums[i][1]]
        ans = ""
        for i in range(10):
            ans += str(i)*numOfNum[i]
        return ans
