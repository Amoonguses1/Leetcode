# Time: O(N)
# Space: O(1)
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val = tickets[k]
        time = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                time += min(ticket, val)
            else:
                time += min(ticket, val-1)
        return time
