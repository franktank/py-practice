"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.path_to(root, p)
        path_q = self.path_to(root, q)
        return self.lca(path_p, path_q)

    def path_to(self, root, node):
        path = list()
        while root:
            path.append(root)
            if root == node:
                return path
            if node.val < root.val:
                root = root.left
            elif node.val > root.val:
                root = root.right

    def lca(self, list_p, list_q):
        repeats = min(len(list_p), len(list_q))
        curr_lca = None
        for i in range(repeats):
            if list_p[i] == list_q[i]:
                curr_lca = list_p[i]
        return curr_lca

    def optimized_lca(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else
                return root
        # Optimization -> prob find curr_lca in path_to simultaneously
