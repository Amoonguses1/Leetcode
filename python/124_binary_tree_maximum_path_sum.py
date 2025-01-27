# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isInputError(self, root):
        if not root:
            return True

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack += node.right, node.left
                if not isinstance(node, TreeNode):
                    return True

        return False

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Function to return max path sum

            Args:
                root(Optional[TreeNode]): a binary tree

            Returns:
                int: max path sum
        """
        if self.isInputError(root):
            raise ValueError("Input must be TreeNode")

        # iterative
        """
        res = float('-inf')
        stack, last, d = [], None, defaultdict(int)
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack[-1]
            if node.right and last != node.right:
                root = node.right
            else:
                node = stack.pop()
                last = node
                d[node] = max(max(d[node.left], d[node.right]) + node.val, 0)
                res = max(res, d[node.left] + d[node.right] + node.val)
        return res
        """
        # recursive
        def dfs(root):
            if not root:
                return [-10**8, 0]

            left, right = dfs(root.left), dfs(root.right)
            path = max(max(left[1], right[1])+root.val, 0)
            tmp = left[1] + right[1] + root.val
            return [max(tmp, left[0], right[0]), path]

        ans = dfs(root)
        return ans[0]
