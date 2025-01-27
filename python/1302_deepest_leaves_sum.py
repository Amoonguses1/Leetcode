# Time: O(N)
# Space: O(N)
# N is the number of nodes
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        stack = deque([(root, 0)])
        depth = 0
        res = 0
        while stack:
            node, cur = stack.popleft()
            if cur > depth:
                res = 0
                depth = cur
            res += node.val
            if node.left:
                stack.append((node.left, cur+1))
            if node.right:
                stack.append((node.right, cur+1))
        return res
