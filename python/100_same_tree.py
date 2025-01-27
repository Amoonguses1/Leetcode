from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Function to check two binary trees if they are same or not
            Args:
                p(Optional[TreeNode]): binary tree
                q(Optional[TreeNode]): binary tree
            Returns:
                bool: if two binary trees are same, return True.
                Otherwise, Return False
        """
        """
        # BFS recursive solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in binary tree
        def preTrav(pTree, qTree):
            if pTree is None and qTree is None:
                return True
            elif pTree is None:
                return False
            elif qTree is None:
                return False

            if pTree.val != qTree.val:
                return False

            return (preTrav(pTree.left, qTree.left)
                    and preTrav(pTree.right, qTree.right))

        return preTrav(p, q)
        """
        # BFS iterative solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in binary tree
        def check(p, q):
            if not p and not q:
                return True

            if not q or not p:
                return False

            if p.val != q.val:
                return False

            return True

        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
