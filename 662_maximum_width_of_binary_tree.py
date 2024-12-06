# Time: O(N)
# Space: O(N)
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        depthPos = dict()
        stack = deque([(root, 0, 0)])
        while stack:
            node, depth, pos = stack.popleft()
            leftMostPos = depthPos.get(depth, -1)
            if leftMostPos != -1:
                res = max(res, pos-leftMostPos+1)
            else:
                depthPos[depth] = pos
            if node.left:
                stack.append((node.left, depth+1, 2*pos))
            if node.right:
                stack.append((node.right, depth+1, 2*pos+1))
        return res
