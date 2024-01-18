# Time: O(M+N)
# Space: O(M+N)
# M and N are the numbers of nodes in the given listnodes
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while l1 or l2:
            if l1 is not None:
                num1 = num1*10 + l1.val
                l1 = l1.next
            if l2 is not None:
                num2 = num2*10 + l2.val
                l2 = l2.next
        head = cur = ListNode(0)
        for digit in str(num1+num2):
            cur.next = ListNode(digit)
            cur = cur.next
        return head.next
