# Time: O(N)
# Space: O(N)
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        cnt = 0
        while head is not None:
            ans.append(0)
            while stack and head.val > stack[-1][0]:
                _, pos = stack.pop()
                ans[pos] = head.val
            stack.append([head.val, cnt])
            cnt += 1
            head = head.next
        return ans
