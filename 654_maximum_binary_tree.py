from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(
            self, nums: List[int]
    ) -> Optional[TreeNode]:
        # Time: O(N^2)
        # Space: O(N)
        # N = len(nums)
        if len(nums) == 0:
            return

        idx = 0
        for i in range(len(nums)):
            if nums[idx] < nums[i]:
                idx = i
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root

    def constructMaximumBinaryTree2(
            self, nums: List[int]
    ) -> Optional[TreeNode]:
        # Time: O(N)
        # Space: O(N)
        # N = len(nums)
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()
            if nodes:
                nodes[-1].right = node
            nodes.append(node)
        return nodes[0]
