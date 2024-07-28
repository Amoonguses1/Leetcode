# Time: O(N)
# Space: O(1)
# N is the number of nodes in the given linked list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        ans = 0
        while node:
            ans = ans*2 + node.val
            node = node.next
        return ans
