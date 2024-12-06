# Time: O(N)
# Space: O(1)
# N = total // cost1


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if total < cost1 and total < cost2:
            return 1

        res = 0
        for i in range((total//cost1) + 1):
            res += (total - cost1*i) // cost2 + 1
        return res
