# Time: O(2**n)
# Space: O(2**n)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Function to generate all well-formed parentheses

            Args:
                n(int): the number of parentheses

            Returns:
                List[str]: all well-formed parentheses
        """
        if not isinstance(n, int):
            raise TypeError("N must be an integer.")

        self.res = []
        self.dfs(0, 0, "", n)
        return self.res

    def dfs(self, left, right, s, n):
        if len(s) == 2 * n:
            self.res.append(s)
            return

        if left < n:
            self.dfs(left+1, right, s+"(", n)
        if right < left:
            self.dfs(left, right+1, s+")", n)
