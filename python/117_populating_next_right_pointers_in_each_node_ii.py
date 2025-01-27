from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """Function to populate each next pointer to
        point to its next right node. If there is no
        next right node, the next pointer is set to
        be NULL
            Args:
                root(Node): tree whose node.next is NULL
            Returns:
                Node: tree whose node.next is not NULL if
                there is next right node
        """

        """
        # BFS iterative
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes
        cur = head = root
        dummy = Node(0)
        while head:
            cur = head
            prev = dummy
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = prev.next
                if cur.right:
                    prev.next = cur.right
                    prev = prev.next
                cur = cur.next
            head = dummy.next
            dummy.next = None
        return root
        """

        # DFS recursion
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes
        def helper(node):
            if not node:
                return

            scanner = node.next
            while scanner:
                if scanner.left:
                    scanner = scanner.left
                    break
                if scanner.right:
                    scanner = scanner.right
                    break
                scanner = scanner.next
            if node.right:
                node.right.next = scanner
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = scanner
            helper(node.right)
            helper(node.left)
            return node
        return helper(root)
