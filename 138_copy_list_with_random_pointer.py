# Time: O(N)
# Space: O(N)
# N is the number of nodes
from collections import defaultdict
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """Function to construct a deep copy of the node

        Args:
            head(Node): a Node

        Returns:
            Node: a deep copy of the Node
        """
        seen = defaultdict(lambda: None)
        cur = head
        while cur:
            if cur not in seen:
                seen[cur] = Node(cur.val)
            if cur.next:
                if cur.next not in seen:
                    seen[cur.next] = Node(cur.next.val)
                seen[cur].next = seen[cur.next]
            if cur.random:
                if cur.random not in seen:
                    seen[cur.random] = Node(cur.random.val)
                seen[cur].random = seen[cur.random]
            cur = cur.next
        return seen[head]
