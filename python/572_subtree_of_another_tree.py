# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True

            stack.append(node.right)
            stack.append(node.left)
        return False

    def isSameTree(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            stack1.append(node1.right)
            stack1.append(node1.left)
            stack2.append(node2.right)
            stack2.append(node2.left)
        if stack1 or stack2:
            return False

        return True
