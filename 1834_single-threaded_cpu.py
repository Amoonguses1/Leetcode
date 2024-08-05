# Time: O(NlogN)
# Space: O(N)
# N = len(tasks)
from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks = sorted([[task[0], task[1], i]
                             for i, task in enumerate(tasks)])
        ans = []
        time = sortedTasks[0][0]
        pos = 0
        available = []
        while len(ans) < len(tasks):
            while pos < len(sortedTasks) and sortedTasks[pos][0] <= time:
                task = sortedTasks[pos]
                heapq.heappush(available, (task[1], task[2]))
                pos += 1
            if len(available) == 0:
                time = sortedTasks[pos][0]
                continue
            processing, idx = heapq.heappop(available)
            time += processing
            ans.append(idx)
        return ans
