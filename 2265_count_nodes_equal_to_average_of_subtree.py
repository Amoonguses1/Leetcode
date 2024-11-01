# Time: O(N)
# Space: O(N)
# N is the number of nodes


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root2sum = dict()

    def averageOfSubtree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        total, num = self.dfs(root)
        res = total // num == root.val
        res += self.averageOfSubtree(root.left)
        res += self.averageOfSubtree(root.right)
        return res

    def dfs(self, root):
        if root is None:
            return 0, 0

        if self.root2sum.get(root, 0):
            return self.root2sum[root]

        total, num = self.dfs(root.left)
        rightave, rightnum = self.dfs(root.right)
        total += rightave + root.val
        num += rightnum + 1
        self.root2sum[root] = [total, num]
        return total, num
