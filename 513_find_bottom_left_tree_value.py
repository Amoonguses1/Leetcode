# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional
# from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS solution
        """
        queue = deque([root])
        leftmost_val = None
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            leftmost_val = node.val
            queue.append(node.right)
            queue.append(node.left)
        return leftmost_val
        """
        # dfs
        _, num = self.searchTree(root, 1)
        return num

    def searchTree(self, root, depth):
        if not root:
            return 0, 0

        rightDepth, rightVal = self.searchTree(root.right, depth+1)
        leftDepth, leftVal = self.searchTree(root.left, depth+1)
        if rightDepth == 0 and leftDepth == 0:
            return depth, root.val

        if rightDepth > leftDepth:
            return rightDepth, rightVal

        return leftDepth, leftVal
