# Time: O(NlogN + MN)
# Space: O(MN)
# N = len(score)
# M = len(score[0])
from typing import List


class Solution:
    def sortTheStudents(
            self, score: List[List[int]], k: int
    ) -> List[List[int]]:
        target = []
        for i, days in enumerate(score):
            target.append((i, days[k]))
        target.sort(key=lambda x: x[1], reverse=True)
        res = [score[i] for i, _ in target]
        return res
