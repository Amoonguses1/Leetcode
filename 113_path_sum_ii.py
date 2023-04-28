# Time: O(N)
# Space: O(N)
# N is the number of node
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode],
                targetSum: int) -> List[List[int]]:
        """Function to return all root-to-leaf paths
        where the sum of the node values in the path equals targetSum

        Args:
            root(Optional[TreeNode]): a binary tree
            targetSum(int): an integer

        Returns:
            List[List[int]]: the list of root-to-leaf paths
        """
        self.ans = []
        self.travpath(root, targetSum, [])
        return self.ans

    def travpath(self, root, rem, path):
        if root:
            if root.left is None and root.right is None and rem == root.val:
                self.ans.append(path+[root.val])
            self.travpath(root.left, rem-root.val, path+[root.val])
            self.travpath(root.right, rem-root.val, path+[root.val])
