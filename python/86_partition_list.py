# Time: O(N)
# Space: O(N)
# N is the number of given nodes
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode],
                  x: int) -> Optional[ListNode]:
        """Function to make partition such that all nodes
        less than x come before nodes greater than or equal to x.

        Args:
            head(Optional[ListNode]): the head of the linked list
            x(int): the integer compared to each nodes

        Returns:
            Optional[ListNode]: the fixed linked list
        """
        less = less_dummy = ListNode()
        greater = greater_dummy = ListNode()
        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                greater.next = ListNode(head.val)
                greater = greater.next
            head = head.next
        less.next = greater_dummy.next
        return less_dummy.next
