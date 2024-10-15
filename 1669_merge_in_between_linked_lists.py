# Time: O(M+N)
# Space: O(1)
# N is the number of nodes in list1
# M is the number of nodes in list2


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
            self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        cur1 = list1
        break_node = cur1
        for i in range(b):
            if i == a - 1:
                break_node = cur1
            cur1 = cur1.next
        cur2 = list2
        while cur2.next:
            cur2 = cur2.next
        break_node.next = list2
        cur2.next = cur1.next
        return list1
