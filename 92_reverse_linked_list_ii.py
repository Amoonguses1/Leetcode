# Time: O(N)
# Space: O(1)
# N is the length of nodes
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode],
                       left: int, right: int) -> Optional[ListNode]:
        """Function to reverse the nodes of the part of the given list

        Args:
            head(Optional[Listnode]): a linked list
            left(int): the start position of reversing the list
            right(int): the end position of reversing the list

        Returns:
            Optional[ListNode]: the reversed linked list
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        for _ in range(left-1):
            cur = cur.next
            pre = pre.next
        for _ in range(right-left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next, pre.next = pre.next, tmp
        return dummy.next
