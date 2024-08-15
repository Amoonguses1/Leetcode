# Time: O(N^2)
# Space: O(N)
# N = len(rains)
from sortedcontainers import SortedList as sl
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullDic = {}
        dryDays = sl()
        ans = []

        for day, rain in enumerate(rains):
            if rain == 0:
                dryDays.add(day)
                ans.append(1)
                continue
            ans.append(-1)
            if rain not in fullDic:
                fullDic[rain] = day
            else:
                if len(dryDays) == 0:
                    return []

                idx = dryDays.bisect_left(fullDic[rain])
                if idx < len(dryDays):
                    ans[dryDays[idx]] = rain
                    fullDic[rain] = day
                    dryDays.remove(dryDays[idx])
                else:
                    return []
        return ans
