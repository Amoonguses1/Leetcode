# Time: O(N)
# Space: O(N)
# N is the number of nodes


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """Function to return a deep copy of the given graph

        Args:
            node('Node'): a connected undirected graph

        Returns:
            'Node': a deep copy of the given graph
        """
        if not node:
            return None

        return self.clone(node, {})

    def clone(self, node, dict):
        if node not in dict:
            dict[node] = Node(node.val, [])
            for n in node.neighbors:
                dict[node].neighbors.append(self.clone(n, dict))
        return dict[node]
