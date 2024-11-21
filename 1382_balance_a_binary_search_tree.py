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
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedLi = []
        self.inOrderTraversal(root, sortedLi)
        return self.construct(sortedLi)

    def inOrderTraversal(self, root, sortedLi):
        if root is None:
            return

        self.inOrderTraversal(root.left, sortedLi)
        sortedLi.append(root.val)
        self.inOrderTraversal(root.right, sortedLi)
        return

    def construct(self, li):
        if len(li) == 0:
            return

        mid = len(li) // 2
        node = TreeNode(li[mid])
        node.left = self.construct(li[:mid])
        node.right = self.construct(li[mid+1:])
        return node
