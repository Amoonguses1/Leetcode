from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Function to swap two adjacent nodes
            Args:
                head(Optional[ListNode]): a singly-linked list
            Returns:
                Optional[ListNode]: the singly-linked list which are changed
        """
        # iterative
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
        """
        # recursive
        # Time: O(N)
        # Space: O(1)
        # N is the number of nodes
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp

        return head
