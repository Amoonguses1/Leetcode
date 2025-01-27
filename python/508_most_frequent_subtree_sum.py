# Time: O(N)
# Space: O(N)
# N is the number of nodes
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        subtreeSum = {}
        self.subTreeSum(subtreeSum, root)
        mostFreq = max(subtreeSum.values())
        return [key for key, val in subtreeSum.items() if val == mostFreq]

    def subTreeSum(self, dic, root):
        if not root:
            return 0

        leftSum = self.subTreeSum(dic, root.left)
        rightSum = self.subTreeSum(dic, root.right)
        curSum = leftSum + rightSum + root.val
        if curSum not in dic:
            dic[curSum] = 0
        dic[curSum] += 1
        return curSum
