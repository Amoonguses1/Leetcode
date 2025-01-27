# Time: O(N^2*logN)
# Space: O(N^2)
# N = len(grid)
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(
            self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.setNode([0, 0], len(grid), grid)

    def setNode(self, top, size, grid):
        if self.isSameGrid(top, size, grid):
            return Node(grid[top[0]][top[1]], True)

        node = Node(grid[top[0]][top[1]], False)
        nxt = []
        for i in [top[0], top[0]+size//2]:
            for j in [top[1], top[1]+size//2]:
                nxt.append([i, j])
        node.topLeft = self.setNode(nxt[0], size//2, grid)
        node.topRight = self.setNode(nxt[1], size//2, grid)
        node.bottomLeft = self.setNode(nxt[2], size//2, grid)
        node.bottomRight = self.setNode(nxt[3], size//2, grid)
        return node

    def isSameGrid(self, top, size, grid):
        for i in range(top[0], top[0]+size):
            for j in range(top[1], top[1]+size):
                if grid[top[0]][top[1]] != grid[i][j]:
                    return False
        return True
