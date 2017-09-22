"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Iterative
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
# Recursive
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > p.val:
            left = self.inorderSuccessor(root.left, p)
            if not left == None:
                return left
            else:
                return root
        else:
            return self.inorderSuccessor(root.right, p)

"""
If root value is greater than p value
    Its a potential successor
    Iterate on by checking if theres a smaller value that could be successor
If root value is less than or equal to p value
    Try to find a value larger
"""
