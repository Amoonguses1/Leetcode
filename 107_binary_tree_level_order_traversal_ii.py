from typing import List
from collections import defaultdict
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Function to build the list which contains
            the bottom-up level order traversal of its nodes' values.
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                List[List[int]]: the bottom-up level order traversal
                    of its nodes' values
        """
        # DFS recursive
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in binary tree
        """
        ans = defaultdict(list)

        def helper(root, height):
            if not root:
                return

            ans[height].append(root.val)
            helper(root.left, height+1)
            helper(root.right, height+1)

        helper(root, 0)
        return reversed(ans.values())
        """

        if not root:
            return
        que = deque([(root, 0)])
        levels = defaultdict(list)
        while que:
            # BFS iterative
            # cur, cur_pos = que.popleft()
            # levels[cur_pos].append(cur.val)
            # if cur.left:
            #     que.append((cur.left, cur_pos+1))
            # if cur.right:
            #     que.append((cur.right, cur_pos+1))

            # DFS
            cur, cur_pos = que.pop()
            levels[cur_pos].append(cur.val)
            if cur.right:
                que.append((cur.right, cur_pos+1))
            if cur.left:
                que.append((cur.left, cur_pos+1))
        return reversed(levels.values())
