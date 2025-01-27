# Time: O(n)
# Space: O(n)
# n is the length of nodes
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # iterative
        if root is None:
            return 0

        nodes = deque()
        nodes.append((root, 1))
        ans = 0
        while nodes:
            node, depth = nodes.popleft()
            ans = depth
            if node.children:
                for child in node.children:
                    nodes.append((child, depth+1))

        return ans

    def maxDepth2(self, root: 'Node') -> int:
        if root is None:
            return 0

        depth = 0
        for node in root.children:
            depth = max(depth, self.maxDepth(node))
        return depth + 1
