"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return list()
        self.paths = []
        self.preorder(root, str(root.val))
        return self.paths

    def preorder(self, root, path):
        if not root.left and not root.right:
            self.paths.append(path)
        if root.left:
            self.preorder(root.left, path + "->" + str(root.left.val))
        if root.right:
            self.preorder(root.right, path + "->" + str(root.right.val))
