# Time: O(N)
# Space: O(N)
# N = len(preorder) = len(postorder)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
            self, preorder: list[int], postorder: list[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(postorder.pop())

        node = TreeNode(postorder.pop())
        index = preorder.index(postorder[-1])

        node.right = self.constructFromPrePost(preorder[index:], postorder)
        node.left = self.constructFromPrePost(preorder[1:index], postorder)
        return node
