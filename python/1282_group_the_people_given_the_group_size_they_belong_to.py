# Time: O(N)
# Space: O(N)
# N = len(groupSizes)
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizesDic = dict()
        for i, size in enumerate(groupSizes):
            li = sizesDic.get(size, [])
            li.append(i)
            sizesDic[size] = li

        ans = []
        for size in sizesDic:
            for i in range(0, len(sizesDic[size]), size):
                ans.append(sizesDic[size][i:i+size])
        return ans
