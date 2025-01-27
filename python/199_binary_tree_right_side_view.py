from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Function to get the list of rightmost node
            in each level
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                List[int]: the list of rightmost node values
                in each level
        """

        """
        # BFS recursion
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        if not root:
            return

        ans = []
        queue = deque([root])
        while queue:
            len_que = len(queue)
            cur_level = []
            for _ in range(len_que):
                cur = queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(cur_level.pop())
        return ans
        """

        # DFS recursive
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes
        ans = []

        def dfs(node, level):
            if not node:
                return

            if len(ans) < level:
                ans.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
            return

        dfs(root, 1)
        return ans
