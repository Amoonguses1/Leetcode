from typing import Optional
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # Time: O(N)
        # Space: O(1)
        value = self.head.val

        i = 2
        node = self.head.next
        while node:
            if random.random() < 1 / i:
                value = node.val
            i += 1
            node = node.next
        return value
