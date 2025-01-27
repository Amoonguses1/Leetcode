# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional, List
from collections import deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        que = deque([[root, 0]])
        curMax = -float('inf')
        ans = []
        level = 0
        while que:
            node, curLevel = que.popleft()
            if not node:
                continue
            if curLevel != level:
                ans.append(curMax)
                level = curLevel
                curMax = node.val
            curMax = max(curMax, node.val)
            que.append([node.left, curLevel+1])
            que.append([node.right, curLevel+1])
        if not math.isinf(curMax):
            ans.append(curMax)
        return ans
