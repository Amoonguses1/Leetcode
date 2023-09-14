# initialize
# Time: O(NlogN)
# Space: O(N)
# update
# Time: O(logN)
# Space: O(logN)
# sumRange
# Time: O(logN)
# space: O(logN)
# N = len(nums)
from typing import List


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        def createTree(nums, left, right):
            if left > right:
                return None

            if left == right:
                n = Node(left, right)
                n.total = nums[left]
                return n

            mid = (left+right) // 2
            root = Node(left, right)
            root.left = createTree(nums, left, mid)
            root.right = createTree(nums, mid+1, right)
            root.total = root.left.total + root.right.total
            return root
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start+root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.total = root.left.total + root.right.total
            return root.total
        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def treeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start+root.end) // 2
            if j <= mid:
                return treeSum(root.left, i, j)
            elif i >= mid + 1:
                return treeSum(root.right, i, j)
            return treeSum(root.left, i, mid) + treeSum(root.right, mid+1, j)
        return treeSum(self.root, left, right)
