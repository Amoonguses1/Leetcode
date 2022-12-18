from typing import List
# use in DFS iterative solution
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Function to get list of tree node values
            from left to right, level by level
            Args:
                root(Optional[TreeNode]): binary tree
            Returns:
                List[List[int]]: the level order traversal of its nodes' values
        """
        """
        # DFS recursive solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        self.ans = []
        self.helper(root, 0)
        return self.ans

    def helper(self, root, depth):
        if root is None:
            return

        if len(self.ans) == depth:
            self.ans.append([])
        self.ans[depth].append(root.val)
        self.helper(root.left, depth+1)
        self.helper(root.right, depth+1)
        """

        # DFS iterative solution
        # Time: O(N)
        # Space: O(N)
        # N is the number of nodes in the binary tree
        if root is None:
            return root

        queue = deque()
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                ans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list
