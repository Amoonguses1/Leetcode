from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """Function to change binary tree into linked list

            Args:
                root(Optional[TreeNode]): binary tree

            Returns:
                None
        """
        if root is not None and not isinstance(root, TreeNode):
            raise ValueError("Input must be a TreeNode.")

        # stack
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        """
        if not root:
            return

        stack = [root.right, root.left]
        vals = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            vals.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        root.left = None
        for val in vals:
            root.right = TreeNode(val)
            root = root.right
        """
        # Morris traversal
        # Time: O(NlogN)
        # Space: O(1)
        # N is the number of nodes
        """
        cur = root
        while cur:
            runner = cur.left
            if runner is not None:
                while runner.right:
                    runner = runner.right
                runner.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        """
        # Recursive
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
