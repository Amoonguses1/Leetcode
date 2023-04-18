# Time: O(N)
# Space: O(1)
# N is the number of nodes
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Function to delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list.

        Args:
            head(Optional{ListNode}): the head of a sorted linked list

        Returns:
            Optional[ListNode]: the sorted linked list
            consist of distinct numbers
        """
        pre = dummy = ListNode()
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre, head = pre.next, head.next
        return dummy.next
