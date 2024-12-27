# Time: O(N)
# Space: O(logN)
# N is the number of nodes in the given tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(
            self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        _, subtree_node = self.getDepthAndDeepestNode(root)
        return subtree_node

    def getDepthAndDeepestNode(
            self, root: Optional[TreeNode]
    ) -> tuple[int, Optional[TreeNode]]:
        if root is None:
            return 0, None

        left_depth, left_node = self.getDepthAndDeepestNode(root.left)
        right_depth, right_node = self.getDepthAndDeepestNode(root.right)

        if left_depth > right_depth:
            return left_depth + 1, left_node
        elif left_depth == right_depth:
            return left_depth + 1, root
        else:
            return right_depth + 1, right_node
