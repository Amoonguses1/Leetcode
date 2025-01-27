# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution
        """
        orderlist = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            orderlist.append(root.val)
            root = root.right
        return orderlist
        """
        # recursive solution
        orderlist = []
        self.dfs(orderlist, root)
        return orderlist

    def dfs(self, li, root):
        if root is None:
            return

        self.dfs(li, root.left)
        li.append(root.val)
        self.dfs(li, root.right)
