# Time:O(n)
# Space :O(n)
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
        leave_nodes = [node for node in adj if len(adj[node]) == 1]
        total = n
        while total > 2:
            total -= len(leave_nodes)
            leave_nxt = []
            for leaf in leave_nodes:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leave_nxt.append(neighbor)
            leave_nodes = leave_nxt
        return leave_nodes
