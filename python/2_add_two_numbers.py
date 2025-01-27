from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        """Function to sum up two numbers
            Args:
                l1(Optional[ListNode]): a digit of the number
                l2(Optional[ListNode]): a digit of the number
            Returns:
                Optional[ListNode]: a digit of the summed-up number
        """
        # recursive
        # Time: O(max(digits1, digits2))
        # Space: O(max(digits1, digits2))
        # digits1 = the digits of the number l1 means
        # digits2 = the digits of the number l2 means
        """
        if l1 is None and l2 is None:
            return -1

        sum = l1.val + l2.val
        digit, carry = sum % 10, sum // 10
        answer = ListNode(digit)
        if any((l1.next, l2.next, carry)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += carry
            answer.next = self.addTwoNumbers(l1, l2)
        return answer
        """
        # iterative
        # Time: O(max(digits1, digits2))
        # Space: O(max(digits1, digits2))
        # digits1 = the digits of the number l1 means
        # digits2 = the digits of the number l2 means
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
