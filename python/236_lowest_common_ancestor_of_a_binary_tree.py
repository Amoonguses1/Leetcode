# Time: O(N)
# Space: O(N)
# N is the number of node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Isvalid(self, root, p, q):
        find = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node == p or node == q:
                find += 1
            if find == 2:
                return True

            stack += node.left, node.right
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        """Function to find lowest common ancestor of two given node
            in a binary tree

            Args:
                root(TreeNode): the root of a binary tree
                p(TreeNode): one of the target node in a binary tree
                q(TreeNode): one of the target node in a binary tree

            Returns:
                TreeNode: lowest common ancestor
        """
        if not self.Isvalid(root, p, q):
            raise ValueError("p or q is not found in root")

        # iterative
        """
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack += node.left, node.right
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            if p in parent and q in parent:
                break
        pParent = set()
        while p:
            pParent.add(p)
            p = parent[p]
        while q:
            if q in pParent:
                return q

            q = parent[q]
        """
        # recursive
        if not root:
            return

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right

        if not right:
            return left

        return root
