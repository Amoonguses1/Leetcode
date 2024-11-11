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
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if node.left:
                stack.append((node.left, node))
                if parent and parent.val % 2 == 0:
                    res += node.left.val
            if node.right:
                stack.append((node.right, node))
                if parent and parent.val % 2 == 0:
                    res += node.right.val
        return res
