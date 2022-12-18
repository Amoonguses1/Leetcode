from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Function to check whether binary tree is
            symmetric around its center
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                bool: if the binary tree is symmmetric, return True.
                Otherwise, Return False
        """
        """
        # BFS recursive solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        def search(root1,root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return (search(root1.left, root2.right)
                        and search(root1.right, root2.left))

        if not root:
            return False

        return search(root.left, root.right)
        """
        # BFS iterative solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        stack = []
        if root:
            stack.append([root.left, root.right])

        while stack:
            left, right = stack.pop()

            if left and right:
                if left.val != right.val:
                    return False

                stack.append([left.left, right.right])
                stack.append([right.left, left.right])

            elif left or right:
                return False

        return True
