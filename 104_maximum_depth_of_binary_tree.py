# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Function to return maximum depth

            Args:
                root(Optional[TreeNode]): binary tree

            Returns:
                int: the maximum depth
        """
        if not isinstance(root, TreeNode) and root:
            raise ValueError("Input must be a tree or Null")

        # iterative
        """
        stack = list()
        depth, tmp = 0, 1
        while root or stack:
            while root:
                stack.append([root, tmp])
                root = root.left
                tmp += 1
            root, tmp = stack.pop()
            depth = max(tmp, depth)
            root = root.right
            tmp += 1
        return depth
        """
        # recursive
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
