# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        traverse_queue = deque()
        traverse_queue.append(root)
        reverse_level = False
        while traverse_queue:
            queue_length = len(traverse_queue)
            arr = []
            for i in range(queue_length):
                node = traverse_queue.popleft()
                if node.left:
                    traverse_queue.append(node.left)
                if node.right:
                    traverse_queue.append(node.right)
                if reverse_level:
                    arr.append(node)
                    self.swapNode(arr, i, queue_length)
            reverse_level = not reverse_level
        return root

    def swapNode(self, arr: List, i: int, length: int):
        if i >= length // 2:
            arr[i].val, arr[length-1-i].val = arr[length-1-i].val, arr[i].val
