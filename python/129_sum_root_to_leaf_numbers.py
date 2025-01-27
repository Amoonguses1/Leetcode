# Time: O(N)
# Space: O(N)
# N is the number of tree nodes
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """Function to calculate the total sum of all root-to-leaf numbers

        Args:
            root(Optional[TreeNode]): a head node of a tree
            in which each node tree represents a digit

        Returns:
            int: the total sum of all root-to-leaf numbers
        """
        return self.dfs(root, 0)

    def dfs(self, root, tmp):
        if not root:
            return 0

        tmp = tmp*10 + root.val
        if not root.left and not root.right:
            return tmp

        return self.dfs(root.left, tmp) + self.dfs(root.right, tmp)
