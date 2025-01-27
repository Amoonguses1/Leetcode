# Time: O(n^k)
# Space: O(n^k)
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """return the list of combinations which sum up target number

        Find all valid combinations of k numbers that sum up to n such
        that the following conditions are true:
        Conminations are consist of only numbers 1 through 9.
        Each number is used at once.

        Args:
            k(int): the number of elements in one combination
            n(int): the target number

        Returns:
            List[List[int]]: the list of combinations
        """
        if k*(k+1)/2 > n:
            return []

        self.ans = []
        self.dfs([], 1, k, n)
        return self.ans

    def dfs(self, li, cur, k, res):
        if k == 0 and res == 0:
            self.ans.append(li)
        if k <= 0 and res <= 0:
            return

        for i in range(cur, 10):
            self.dfs(li+[i], i+1, k-1, res-i)
