class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """Function to populate each next pointer to point to its next
            right node. If there is no next right node, the next pointer
            should be set to NULL.
            Args:
                root(Optional[Node]): perfect binary tree whose class is Node
                    without next pointer
            Returns:
                Optional[Node]: perfect binary tree whose class is Node
                    populated next pointer

        """
        # BFS
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes in tree
        """
        if root is None:
            return

        node = root
        while node.left:
            head = node
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            node = node.left
        return root
        """
        # DFS
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes in tree
        self.dfs(root)
        return root

    def dfs(self, node):
        if node is None or node.left is None:
            return

        node.left.next = node.right
        if node.next is not None:
            node.right.next = node.next.left
        self.dfs(node.left)
        self.dfs(node.right)
