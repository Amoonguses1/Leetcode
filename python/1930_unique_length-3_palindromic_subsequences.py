# Time: O(MN)
# Space: O(N)
# N = len(s) M is the number of character types


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        posDict = dict()
        for i, ch in enumerate(s):
            li = posDict.get(ch, [])
            if len(li) < 2:
                li.append(i)
            else:
                li[1] = i
            posDict[ch] = li

        ans = 0
        for positions in posDict.values():
            if len(positions) < 2 or self.isAdjacent(positions):
                continue
            ans += len(set(s[positions[0]+1:positions[1]]))
        return ans

    def isAdjacent(self, positions: list[int]) -> bool:
        return positions[1] == positions[0] + 1
