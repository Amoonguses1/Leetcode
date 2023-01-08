from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Function to reconstruct Linked-list
            Args:
                head(Optional[ListNode]): the start node of the linked-list
        """
        if head is None:
            return

        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        slow.next = None
        first_half = head
        second_half = prev
        while first_half and second_half:
            first_next = first_half.next
            second_next = second_half.next
            second_half.next = first_half.next
            first_half.next = second_half
            first_half = first_next
            second_half = second_next
        if first_half:
            first_half.next = None
        """
        # recursion
        # Time: O(N)
        # Space: O(1), don't count function call stack
        # N is the number of nodes
        def helper(head, tail, stack):
            if head is tail:
                head.next = None
                return

            if head.next is tail:
                tail.next = None
                return

            tailprev = stack.pop()
            headnext = head.next
            head.next = tail
            tail.next = headnext
            helper(headnext, tailprev, stack)

        dummy = head
        stack = []
        while dummy is not None:
            stack.append(dummy)
            dummy = dummy.next
        tail = stack.pop()
        helper(head, tail, stack)
