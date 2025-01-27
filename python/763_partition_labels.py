from typing import List
# Time: O(N)
# Space: O(M)
# N = len(s), M is the number of type of character


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chPos = dict()
        for i, ch in enumerate(s):
            chPos[ch] = i
        ans = []
        start, end = 0, chPos[s[0]]
        for i, ch in enumerate(s):
            end = max(end, chPos[ch])
            if i == end:
                ans.append(end-start+1)
                start = end + 1
        if len(s) != start:
            ans.append(end-start+1)
        return ans
