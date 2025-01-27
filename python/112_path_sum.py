from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Function to judge if the tree has a root-to-leaf path
            such that adding up all the values along the path equals targetSum.
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                bool: return True if the tree has a root-to-leaf path such that
                    adding up all the values along the path equals targetSum,
                    else return False.
        """
        # BFS iterative
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        """
        deq = deque([(root, targetSum)])
        while deq:
            # if you replace pop() into popleft(), then this solution
            # is changed to DFS
            root, res = deq.pop()
            if not root:
                continue
            res -= root.val
            if res == 0 and not root.left and not root.right:
                return True

            deq.append((root.left, res))
            deq.append((root.right, res))
        return False
        """
        # DFS recursive
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return (self.hasPathSum(root.left, sum - root.val)
                or self.hasPathSum(root.right, sum - root.val))
