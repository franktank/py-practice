"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
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
        self.parents = {}
        self.parents[root] = None
        self.preorder(root)
        pp = []
        pq = []
        while p:
            pp.insert(0, p)
            p = self.parents[p]
        while q:
            pq.insert(0, q)
            q = self.parents[q]
        m = min(len(pp), len(pq))
        ret = None
        for i in range(m):
            if pp[i] == pq[i]:
                ret = pp[i]
        return ret

    def preorder(self, root):
        if root.left:
            self.parents[root.left] = root
            self.preorder(root.left)
        if root.right:
            self.parents[root.right] = root
            self.preorder(root.right)
