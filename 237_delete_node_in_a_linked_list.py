# Time: O(1)
# Space: O(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """Delete a node from a singly-linked list

        Delete the given node and do not access the firstv node of head

        Args:
            node(ListNode): the node to be deleted

        Returns:
            None
        """
        node.val = node.next.val
        node.next = node.next.next
