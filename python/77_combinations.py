# Time: O(pow(n,k))
# Space: O(pow(n,k))
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Function to return all possible combinations of k numbers
        from 1 to n.

        Args:
            n(int): the max integer of candidates
            k(int): the upper limit of candidates integer

        Returns:
            List[List[int]]: all possible combinations
        """
        res, cur = [], []

        def dfs(start, remain):
            if remain == 0:
                res.append(cur.copy())
                return

            for i in range(start, n):
                cur.append(i+1)
                dfs(i+1, remain-1)
                cur.pop()
        dfs(0, k)
        return res
