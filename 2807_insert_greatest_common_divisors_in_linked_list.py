# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def calcGCD(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
        node = head
        while node and node.next:
            gcd = calcGCD(node.val, node.next.val)
            gcdNode = ListNode(gcd)
            tmp = node.next
            node.next = gcdNode
            gcdNode.next = tmp
            node = node.next.next
        return head
