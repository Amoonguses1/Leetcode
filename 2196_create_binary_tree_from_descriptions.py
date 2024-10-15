# Time: O(N)
# Space: O(N)
# N = len(descriptions)
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(
            self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodeDic = dict()
        parentDict = dict()
        for parent, child, isLeft in descriptions:
            node = nodeDic.get(parent, TreeNode(parent))
            if not nodeDic.get(parent, False):
                nodeDic[parent] = node
            childNode = nodeDic.get(child, TreeNode(child))
            parentDict[child] = node
            if not nodeDic.get(child, False):
                nodeDic[child] = childNode
            if isLeft:
                node.left = childNode
            else:
                node.right = childNode
        root = parentDict.get(descriptions[0][0], False)
        while root and parentDict.get(root.val, False):
            root = parentDict.get(root.val, False)
        return root if root else nodeDic[descriptions[0][0]]
