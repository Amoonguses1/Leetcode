# Time: O(N)
# Space: O(N)
# N is the number of node
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # iterative
        """
        stack = deque([root])
        res = ""
        while stack:
            node = stack.popleft()
            if node is None:
                res += "null,"
            else:
                res += str(node.val) + ","
                stack.append(node.left)
                stack.append(node.right)
        return res[:-1]
        """
        # recursive
        if not root:
            return 'x'

        return ','.join([str(root.val), self.serialize(root.left),
                         self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # iterative
        """
        stack = data.split(",")
        stack = deque(stack)
        if stack[0] == "null":
            return

        head = TreeNode(int(stack.popleft()))
        stack_build = deque([head])
        l_r = 0
        while stack:
            val = stack.popleft()
            if val == "null":
                l_r += 1
                if l_r % 2 == 0:
                    stack_build.popleft()
                continue
            node = stack_build.popleft()
            if l_r % 2 == 0:
                node.left = TreeNode(int(val))
                stack_build.appendleft(node)
                stack_build.append(node.left)
            else:
                node.right = TreeNode(int(val))
                stack_build.append(node.right)
            l_r += 1
        return head
        """
        # recursive
        self.data = data
        if self.data[0] == 'x':
            return None

        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])
        return node
