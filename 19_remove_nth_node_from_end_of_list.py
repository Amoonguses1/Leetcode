# Time: O(N)
# # Space: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        """Function to remove Nth node from last node
            Args:
                head(Optional[ListNode]): a linked list
                n(int): the target node number
            Returns:
                Optional[ListNode]: the linked list removed nth
                    node from last node
        """
        if type(head) != type(ListNode(0)):
            raise ValueError("Input must be linked list")

        if not isinstance(n, int) or n < 1:
            raise ValueError("n must be a natural number")

        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
