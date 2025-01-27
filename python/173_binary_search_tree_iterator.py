from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """A class that represents an iterator over the in-order traversal
    of a bianry search tree.

    'next' and 'hasNext' functions are called when using.

    Tipical usage

        obj = BSTIterator(root)
        param_1 = obj.next()
        param_2 = obj.hasNext()
    """
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeftNodes(root)

    def next(self) -> int:
        """Move the pointer to the right.

        Move the pointer to the right node,
        then return the next node number

        Args:
            None

        Returns:
            int: the next nodes pointer value
        """
        # Time: O(logN)
        # N is the number of nodes
        # Space: O(1)
        cur = self.stack.pop()
        self.pushLeftNodes(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        """Check if there is a next node

        Return true if there exists a number in the traversal
        to the right of the pointer, else return False.

        Args:
            None

        Returns:
            boolean: whether the pointer can move to the next pointer
        """
        # Time: O(1)
        # Space: O(1)
        return True if self.stack else False

    def pushLeftNodes(self, root):
        # Time: O(logN)
        # Space: O(logN)
        # N is the number of nodes
        while root:
            self.stack.append(root)
            root = root.left
