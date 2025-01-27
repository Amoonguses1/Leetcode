from typing import List
from collections import deque
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Function to return the zigzag level order traversal
            of its nodes' values.
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                List[List[int]]: The list of node values
                is sorted by zigzag at each level.
        """
        # BFS iterative
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in binary tree
        """
        if root is None:
            return
        que = deque([root])
        ret = []
        even_check = False
        while que:
            level = []
            length = len(que)
            for _ in range(length):
                cur = que.popleft()
                level.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            if even_check:
                ret.append(reversed(level))
            else:
                ret.append(level)
            even_check = not even_check
        return ret
        """
        # DFS recursive
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in binary tree
        ret = defaultdict(list)

        def recursive(node, height):
            if node:
                ret[height].append(node.val)
                recursive(node.left, height+1)
                recursive(node.right, height+1)

        recursive(root, 0)
        ans = []
        for idx in ret.keys():
            if idx % 2 == 0:
                ans.append(ret[idx])
            else:
                ans.append(reversed(ret[idx]))
        return ans
