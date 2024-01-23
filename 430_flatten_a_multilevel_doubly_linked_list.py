# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        headNode = Node(head.val)
        flatterNode = headNode
        searchNode = head
        stack = []
        while searchNode.child or searchNode.next or stack:
            if searchNode.child:
                if searchNode.next:
                    stack.append(searchNode.next)
                searchNode = searchNode.child
            elif searchNode.next:
                searchNode = searchNode.next
            elif stack:
                searchNode = stack.pop()
            flatterNode.next = Node(searchNode.val)
            flatterNode.next.prev = flatterNode
            flatterNode = flatterNode.next
        return headNode
