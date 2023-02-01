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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Function to return invert the binary tree

            Args:
                root(Optional[TreeNode]): binary tree

            Returns:
                Optional[TreeNode]: inverted binary tree
        """
        if not isinstance(root, TreeNode) and root:
            raise ValueError("Input must be a tree or Null")

        # iterative
        """
        if not root:
            return root

        head = TreeNode(root.val)
        stack, stack_inv = [root], [head]
        while stack:
            node, dummy = stack.pop(), stack_inv.pop()
            if node:
                stack += node.left, node.right
                if node.left:
                    dummy.right = TreeNode(node.left.val)
                if node.right:
                    dummy.left = TreeNode(node.right.val)
                stack_inv += dummy.right, dummy.left
        return head
        """
        if not root:
            return

        return TreeNode(root.val, self.invertTree(root.right),
                        self.invertTree(root.left))
