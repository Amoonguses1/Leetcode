# Time: O(N)
# Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        cur = dummy = ListNode(0)
        while head:
            if head.val == 0:
                cur.next = ListNode(val)
                val = 0
                cur = cur.next
            else:
                val += head.val
            head = head.next
        return dummy.next.next
