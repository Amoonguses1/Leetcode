# Time: O(n^2)
# Space: O(n_C_(n/2)/(n/2+1))  Catalan number
from typing import List
from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """Function to find all possible full binary trees
            Args:
                n(int): the number of nodes in binary trees
            Returns:
                List[Optional[TreeNode]]: the list of all possible full
                binary trees consist of n nodes
        """
        return self.dp(n, defaultdict(list))

    def dp(self, n, memo):
        if not n % 2:
            return list()

        if n in memo:
            return memo[n]

        if n == 1:
            memo[n].append(TreeNode(0))
            return memo[n]

        for i in range(1, n-1):
            left_li, right_li = self.dp(i, memo), self.dp(n-1-i, memo)
            if not left_li or not right_li:
                continue

            for left in left_li:
                for right in right_li:
                    head = TreeNode(0, left, right)
                    memo[n].append(head)
        return memo[n]
