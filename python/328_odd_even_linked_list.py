from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the given ListNode
        """
        if head is None:
            return None

        iterate, even = head, ListNode(0)
        cur, prev = even, iterate
        while iterate and iterate.next:
            cur.next = iterate.next
            iterate.next = cur.next.next
            cur = cur.next
            prev = iterate
            iterate = iterate.next
        cur.next = None
        if iterate:
            iterate.next = even.next
        else:
            prev.next = even.next
        return head
        """
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes in the given ListNode
        if head is None:
            return None

        odd, even = head, head.next
        evenHead = even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head
