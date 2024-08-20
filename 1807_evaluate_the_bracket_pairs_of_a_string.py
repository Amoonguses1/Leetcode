# Time: O(N+M)
# Space: O(N+M)
# N = len(s), M = len(knowledge)
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        replaceDict = dict()
        for key, val in knowledge:
            replaceDict[key] = val
        replacedString = ""
        left = 0
        for i, ch in enumerate(s):
            if ch == "(":
                replacedString += s[left: i]
                left = i + 1
            if ch == ")":
                key = s[left:i]
                replacedString += replaceDict.get(key, "?")
                left = i + 1
        return replacedString + s[left:]
