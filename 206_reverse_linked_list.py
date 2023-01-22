from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Function to reverse linked list
            Args:
                head(Optional[ListNode]): a Linked-list
            Returns:
                Optional[ListNode]: a reversed linked list
        """
        if type(head) != ListNode(0) or head is not None:
            raise ValueError("Input must be type: ListNode")

        # iterative solution
        # Time: O(N)
        # Space: O(1)
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        """
        # recursive solution
        # Time: O(N)
        # Space: O(N)
        if head is None or head.next is None:  # head = 2 & 2 -> 3
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
